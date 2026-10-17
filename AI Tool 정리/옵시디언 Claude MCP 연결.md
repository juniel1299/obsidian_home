# 옵시디언 + Claude Code MCP 연결
2026-10-16 ~ 17 에 직접 연결하면서 정리한 내용

Claude Code 를 볼트 폴더에서 열면 파일은 원래 읽고 쓸 수 있음
MCP 를 붙이면 옵시디언 기능 (검색 , 태그 검색 , frontmatter , 최근 변경 노트 등) 을 도구로 쓸 수 있게 됨

## 준비물
- 옵시디언 커뮤니티 플러그인 **Local REST API** (작성자 Adam Coddington)
  - 내가 설치한 버전 : `Local REST API with MCP` v5.4.0
- MCP 서버 : **mcp-obsidian** (uvx 로 실행 , 파이썬 패키지)
- uv 설치되어 있어야 함 (`brew install uv`)

## 연결 순서
1. 옵시디언 → 설정 → 커뮤니티 플러그인 → 탐색 → `Local REST API` 설치
2. **활성화 토글까지 켜기** (설치만 하면 동작 안 함)
3. 설정 → Local REST API → API Key 복사
4. 터미널에서 등록
```bash
claude mcp add obsidian -s user -e OBSIDIAN_API_KEY=<API_KEY> -- uvx mcp-obsidian
```
5. 확인
```bash
claude mcp list
# obsidian: uvx mcp-obsidian - ✔ Connected
```
6. Claude Code 세션 새로 시작 → obsidian 도구가 붙음

기본 접속 주소 : `https://127.0.0.1:27124` (자체 서명 인증서)
포트 바꿨으면 `-e OBSIDIAN_PORT=포트` 추가

## 플러그인 동작 확인 (curl)
```bash
# 인증 없이 : 플러그인 정보 (status OK 나오면 플러그인 정상)
curl -sk https://127.0.0.1:27124/

# 인증 : 볼트 루트 파일 목록
curl -sk -H "Authorization: Bearer <API_KEY>" https://127.0.0.1:27124/vault/
```
-k 는 자체 서명 인증서라 검증을 끄는 옵션

## 쓸 수 있게 되는 도구 (mcp-obsidian)
- list_files_in_vault , list_files_in_dir : 파일 목록
- get_file_contents , batch_get_file_contents : 노트 읽기
- simple_search , complex_search : 검색
- search_by_tag , get_frontmatter : 태그 , frontmatter
- get_recent_changes : 최근 수정 노트
- put_content , append_content , patch_content : 노트 쓰기 / 덧붙이기 / 부분 수정
- delete_file : 삭제
- get_periodic_note , get_recent_periodic_notes : 데일리 노트

## 겪은 문제
### 1. claude mcp add 했는데 등록이 안 됨
- `claude mcp get obsidian` → `No MCP server named "obsidian"`
- 원인 : 명령이 실제로 실행되지 않았음 (실행 후 아래 메시지가 나와야 성공)
```
Added stdio MCP server obsidian with command: uvx mcp-obsidian to user config
File modified: /Users/wonjun/.claude.json
```

### 2. 플러그인 설치했는데 응답이 없음
- `curl https://127.0.0.1:27124/` → 응답 없음 , 27124 포트 LISTEN 없음
- 원인 : 설치만 하고 활성화를 안 했음 → `.obsidian/community-plugins.json` 에 플러그인 id 가 없었음
- 활성화 후 바로 해결

### 3. API 키가 GitHub 에 올라감 (가장 중요)
- 플러그인 설정 파일 `.obsidian/plugins/obsidian-local-rest-api/data.json` 에 **API 키 + TLS 개인키** 가 저장됨
- 볼트를 obsidian-git 으로 1분마다 자동 커밋 + push 하고 있었음
- → 플러그인 활성화 1분 만에 data.json 이 커밋되어 GitHub 에 push 됨

해결
```bash
# 1. 앞으로 안 올라가게 ignore 추가
echo ".obsidian/plugins/obsidian-local-rest-api/data.json" >> .gitignore

# 2. git 추적만 해제 (파일은 그대로 남음)
git rm --cached .obsidian/plugins/obsidian-local-rest-api/data.json
```
3. 플러그인 설정 → **Reset all crypto** 버튼 → API 키 , 인증서 , 개인키 전부 재발급
   - 반드시 1, 2번 다음에 해야 함 (먼저 하면 새 키도 push 됨)
4. 새 키로 MCP 다시 등록 (`claude mcp remove obsidian -s user` 후 add)

API 는 127.0.0.1 에서만 열려 있어서 외부에서 바로 악용되긴 어렵지만 , 키는 무조건 재발급
예전 키는 git 히스토리에 남음 → 공개 저장소면 비공개 전환이나 히스토리 정리 필요

**교훈 : obsidian-git 쓰는 사람은 비밀값 저장하는 플러그인 설치 전에 .gitignore 부터**

## 참고
- 플러그인 자체에도 MCP 엔드포인트가 있음 (`https://127.0.0.1:27124/mcp` , 인증 필요)
  - HTTP 방식으로 바로 붙일 수도 있지만 자체 서명 인증서 문제가 있어서 mcp-obsidian 사용함 (직접 테스트는 안 해봄)
- MCP 는 **옵시디언이 켜져 있을 때만** 동작함
- 키 재발급하면 MCP 등록도 다시 해야 함
