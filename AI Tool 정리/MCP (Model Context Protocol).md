# MCP (Model Context Protocol)
AI 모델이 외부 도구 , 데이터에 접근하는 방식을 표준화한 오픈 프로토콜
2024년 11월 Anthropic 이 공개함 .

## 왜 필요한가
AI 는 학습한 내용 + 대화 내용만 알고 있음 → 내 파일 , DB , 서비스 데이터는 모름

기존엔 서비스마다 연결 코드를 따로 만들어야 했음
(AI 앱 N개 × 서비스 M개 = N×M 개의 연동)

MCP 로 규격을 통일하면 서비스는 MCP 서버 하나만 만들고 , AI 앱은 MCP 클라이언트 하나만 만들면 됨
(N + M 개로 줄어듦)

→ 흔히 **AI 용 USB-C** 라고 비유함 (충전기 규격 통일처럼)

## 구성 요소
- **Host (호스트)** : 사용자가 쓰는 AI 앱 (Claude Desktop , Claude Code , IDE 등)
- **Client (클라이언트)** : 호스트 안에서 MCP 서버 하나와 1:1 로 연결을 유지하는 부분
- **Server (서버)** : 실제 기능을 제공하는 프로그램 (옵시디언 , GitHub , 파일시스템 등)

호스트 하나가 여러 서버에 동시에 연결 가능 (서버마다 클라이언트가 하나씩)

## 서버가 제공하는 것
- **Tools (도구)** : AI 가 호출하는 함수 (예 : 노트 검색 , 파일 쓰기)
- **Resources (리소스)** : AI 가 읽을 수 있는 데이터 (예 : 파일 내용)
- **Prompts (프롬프트)** : 미리 만들어 둔 프롬프트 템플릿

실제로 가장 많이 쓰는 건 Tools

## 통신 방식
메시지 형식은 JSON-RPC 2.0

전송 방식 (transport) 2가지
- **stdio** : 호스트가 서버를 내 컴퓨터에서 프로세스로 실행 , 표준 입출력으로 통신 (로컬용)
- **Streamable HTTP** : 서버가 HTTP 로 떠 있고 원격으로 연결 (원격용)

## Claude Code 에서 등록하기
```bash
# stdio 서버
claude mcp add <이름> -- <실행 명령>

# 환경변수 (API 키 등) 전달
claude mcp add <이름> -e KEY=값 -- <실행 명령>

# HTTP 서버
claude mcp add --transport http <이름> <URL>

# 목록 / 상태 확인
claude mcp list
claude mcp get <이름>
```

범위 (scope)
- local (기본) : 현재 프로젝트 , 나만
- project : 프로젝트의 .mcp.json 에 저장 → git 으로 팀과 공유
- user : 모든 프로젝트에서 사용 (~/.claude.json)

API 키가 들어가는 서버는 project 범위에 키를 직접 쓰면 git 에 올라감 → user 범위나 환경변수 사용

## 주의
- MCP 서버는 내 컴퓨터에서 실행되는 프로그램 → 믿을 수 있는 서버만 설치
- 등록 후 **세션을 새로 시작해야** 도구가 붙음
