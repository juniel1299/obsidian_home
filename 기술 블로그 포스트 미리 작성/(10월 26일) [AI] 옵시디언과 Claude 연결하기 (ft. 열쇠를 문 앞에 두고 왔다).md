## 내 노트를 AI 가 읽는다면 ?

공부한 내용은 전부 옵시디언에 정리하고 있다.
그런데 노트가 350개를 넘어가니까 이런 생각이 들었다.

> "이 노트들 중에 블로그에 쓸 만한 걸 AI 가 골라주면 좋겠는데…?"

그래서 옵시디언과 Claude 를 **MCP** 로 연결해 봤다.
연결 자체는 10분이면 끝나는데, 그 과정에서 **API 키를 GitHub 에 올리는 사고**까지 쳤다. 그 이야기까지 같이 정리한다.

(MCP 가 뭔지 모른다면 이전 글 [MCP (Model Context Protocol)](https://problem-child.tistory.com/125) 을 먼저 보고 오면 좋습니다)

---

## 구조

```
Claude Code ──(MCP)── mcp-obsidian ──(HTTPS)── Local REST API 플러그인 ── 옵시디언 볼트
 (호스트)              (MCP 서버)                 (옵시디언 안에서 실행)
```

- **Local REST API** : 옵시디언 안에서 REST API 서버를 띄워주는 커뮤니티 플러그인
- **mcp-obsidian** : 그 REST API 를 MCP 도구로 바꿔주는 MCP 서버
- **Claude Code** : MCP 서버를 호출하는 AI (호스트)

### 굳이 MCP 가 필요한가 ?

사실 Claude Code 를 볼트 폴더에서 실행하면 파일은 원래 읽고 쓸 수 있다.
MCP 를 붙이면 여기에 **옵시디언 기능**이 추가된다.

- 옵시디언 검색 엔진으로 노트 검색
- 태그 검색 , frontmatter 읽기
- 최근 수정한 노트 목록
- 데일리 노트 읽기

---

## 준비물

- 옵시디언 (데스크톱)
- Claude Code
- uv (파이썬 패키지 실행 도구 , mcp-obsidian 을 uvx 로 실행함)

```bash
brew install uv
```

---

## 연결하기

### 1. 플러그인 설치 + 활성화

옵시디언 → 설정 → 커뮤니티 플러그인 → 탐색 → `Local REST API` 검색 → 설치

여기서 **활성화 토글까지 꼭 켜야 한다.**
(설치만 하고 넘어갔다가 한참을 헤맸다. 아래 "삽질 기록" 참고)

활성화하면 `https://127.0.0.1:27124` 에서 API 서버가 뜬다.

### 2. API 키 복사

설정 → Local REST API → **API Key** 복사

### 3. MCP 서버 등록

터미널에서 실행한다. `<API_KEY>` 자리에 복사한 키를 넣는다.

```bash
claude mcp add obsidian -s user -e OBSIDIAN_API_KEY=<API_KEY> -- uvx mcp-obsidian
```

- `obsidian` : MCP 서버 이름 (마음대로)
- `-s user` : 모든 프로젝트에서 사용 (설정이 `~/.claude.json` 에 저장됨)
- `-e` : 환경변수로 API 키 전달
- `--` 뒤 : MCP 서버를 실행할 명령

성공하면 이런 메시지가 나온다.

```
Added stdio MCP server obsidian with command: uvx mcp-obsidian to user config
```

포트를 바꿨다면 `-e OBSIDIAN_PORT=포트` 를 추가하면 된다.

### 4. 연결 확인

```bash
claude mcp list
# obsidian: uvx mcp-obsidian - ✔ Connected
```

Connected 가 뜨면 끝
Claude Code 세션을 **새로 시작해야** 도구가 붙는다.

---

## 쓸 수 있는 도구

| 도구 | 기능 |
|---|---|
| list_files_in_vault , list_files_in_dir | 파일 목록 |
| get_file_contents , batch_get_file_contents | 노트 읽기 (여러 개 한 번에) |
| simple_search , complex_search | 검색 |
| search_by_tag , get_frontmatter | 태그 , frontmatter |
| get_recent_changes | 최근 수정한 노트 |
| put_content , append_content , patch_content | 노트 쓰기 , 덧붙이기 , 부분 수정 |
| delete_file | 삭제 |
| get_periodic_note | 데일리 노트 |

이제 "최근 일주일 동안 수정한 노트 보여줘" , "#react 태그 노트 찾아줘" 같은 요청이 가능하다.

---

## 삽질 기록

### 1. 등록했는데 등록이 안 됨

```bash
claude mcp get obsidian
# No MCP server named "obsidian"
```

명령을 실행했다고 생각했는데 실제로는 실행이 안 됐었다.
위의 **Added stdio MCP server ...** 메시지가 안 나왔다면 등록이 안 된 거다.

### 2. 플러그인이 응답하지 않음

```bash
curl -sk https://127.0.0.1:27124/
# 응답 없음
```

플러그인을 **설치만 하고 활성화를 안 했다.**
활성화하자마자 바로 응답이 왔다.

```bash
curl -sk https://127.0.0.1:27124/
# { "status": "OK", ... }
```

(-k 는 플러그인이 자체 서명 인증서를 쓰기 때문에 인증서 검증을 끄는 옵션)

API 키까지 맞는지 확인하고 싶으면

```bash
curl -sk -H "Authorization: Bearer <API_KEY>" https://127.0.0.1:27124/vault/
```

볼트 파일 목록이 나오면 정상이다.

### 3. API 키를 GitHub 에 올려버림 (제일 중요)

이번 글을 쓴 진짜 이유

나는 볼트를 **obsidian-git** 플러그인으로 GitHub 에 백업하고 있다.
1분마다 자동으로 커밋 + push 하는 설정이다.

그런데 Local REST API 플러그인은 설정 파일에 이런 걸 저장한다.

```
.obsidian/plugins/obsidian-local-rest-api/data.json
 ├─ apiKey       ← API 키
 ├─ privateKey   ← TLS 개인키
 └─ ...
```

결과는 예상대로
플러그인을 켜고 **1분 만에** API 키와 개인키가 GitHub 에 올라갔다.

열쇠를 문 앞에 두고 온 셈이다.

---

## 해결 방법

순서가 중요하다.

### 1. .gitignore 에 추가

```bash
echo ".obsidian/plugins/obsidian-local-rest-api/data.json" >> .gitignore
```

### 2. git 추적 해제

```bash
git rm --cached .obsidian/plugins/obsidian-local-rest-api/data.json
```

`--cached` 를 붙이면 **git 에서만 빠지고 파일은 그대로 남는다.**
(안 붙이면 파일이 삭제되니 주의)

### 3. 키 재발급

플러그인 설정 → **Reset all crypto** 버튼
API 키 , 인증서 , 개인키가 한 번에 새로 만들어진다.

**반드시 1, 2번 다음에 해야 한다.**
먼저 재발급하면 새 키가 또 1분 뒤에 push 된다.

### 4. MCP 다시 등록

키가 바뀌었으니 MCP 등록도 다시 한다.

```bash
claude mcp remove obsidian -s user
claude mcp add obsidian -s user -e OBSIDIAN_API_KEY=<새 API_KEY> -- uvx mcp-obsidian
```

### 그래도 남는 것

예전 키는 **git 히스토리에 그대로 남아 있다.**
나는 키를 재발급해서 예전 키가 무효가 됐으니 그대로 뒀지만, 저장소가 공개라면 비공개로 바꾸거나 히스토리를 정리하는 것도 고려해야 한다.

다행히 이 API 는 `127.0.0.1` (내 컴퓨터) 에서만 열려 있어서 외부에서 바로 악용하기는 어렵다.
그래도 키는 무조건 재발급하자.

---

## 정리

| 단계 | 할 일 |
|---|---|
| 1 | Local REST API 플러그인 설치 + **활성화** |
| 2 | obsidian-git 쓰는 중이면 **data.json 을 .gitignore 에 먼저 추가** |
| 3 | API 키 복사 |
| 4 | `claude mcp add obsidian -s user -e OBSIDIAN_API_KEY=<API_KEY> -- uvx mcp-obsidian` |
| 5 | `claude mcp list` 로 Connected 확인 → 세션 재시작 |

주의할 점

- MCP 는 **옵시디언이 켜져 있을 때만** 동작한다
- 키를 재발급하면 MCP 도 다시 등록해야 한다
- **obsidian-git 사용자는 비밀값을 저장하는 플러그인을 설치하기 전에 .gitignore 부터**

다음 글에서는 이렇게 연결한 Claude 로 옵시디언 노트를 블로그 글로 만드는 과정을 정리해 보려고 한다.
