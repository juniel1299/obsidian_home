# Obscura
AI 에이전트 + 웹 스크래핑 위해 만들어진 브라우저   
## 요약
Rust + V8 자바 스크립트 엔진  
내용만 가져와서 뿌리는 형식 (그래픽 요소 x).      
크롬에 80% 가벼움 -> 토큰 사용량 적음  

### 설치법
1. docker 사용하여 설치 ( 터미널에 해당 내용 작성 )   
``` cmd
docker run -d --name obscura -p 127.0.0.1:9222:9222 h4ckf0r0day/obscura  
```


2. 사전 빌드 바이너리 다운로드
```cmd
# 최신 릴리즈 확인: https://github.com/h4ckf0r0day/obscura/releases 
# Linux x86_64 (렌더링 + 스텔스 포함) 
wget https://github.com/h4ckf0r0day/obscura/releases/download/v0.2.1/obscura-x86_64-linux-stealth.tar.gz 
tar xzf obscura-x86_64-linux-stealth.tar.gz 
./obscura --help
```

3. 소스 컴파일 (Rust 필요)
```cmd
git clone https://github.com/h4ckf0r0day/obscura.git 
cd obscura 
# 렌더링만 (기본) 
cargo build --release -p obscura-cli --bins --features render 
# 렌더링 + 스텔스 모드 cargo build --release -p obscura-cli --bins --features render,stealth 
# 렌더링 없음 (경량) cargo build --release -p obscura-cli --bins --no-default-features
```

### 사용법
``` md

# 페이지 제목 가져오기 
obscura fetch https://example.com --eval "document.title" 

# 모든 링크 추출 
obscura fetch https://example.com --dump links 

# JS 렌더링 후 HTML 덤프 
obscura fetch https://news.ycombinator.com --dump html 

# 텍스트만 추출해서 파일로 저장 
obscura fetch https://example.com --dump text --output page.txt 

# 스크린샷 캡처 
obscura fetch https://example.com --screenshot page.png 

# 프록시 통해 요청 
obscura --proxy socks5://127.0.0.1:1080 fetch https://example.com --dump text 

# 동적 콘텐츠 기다리기 
obscura fetch https://example.com --wait-until networkidle0 

# 타임아웃 설정 (초) 
obscura fetch https://example.com --timeout 10

로컬 개발 서버 접근 (SSRF 차단 방지) 
obscura fetch http://127.0.0.1:3000 --allow-private-network --dump text
```

