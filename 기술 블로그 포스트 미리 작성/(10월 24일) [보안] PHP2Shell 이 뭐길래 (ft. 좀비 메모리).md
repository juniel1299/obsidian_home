## 인터넷의 70% 가 비상

2026년 10월 21일, PHP 에 긴급 패치가 나왔다.

> "인증 없이, 원격에서, 서버에 아무 코드나 실행할 수 있다"

보안 취약점 중에서도 제일 무서운 조합이다.
이름은 **PHP2Shell** (CVE-2026-109618 , CVE-2026-109619)
심각도는 CVSS 4.0 기준 **9.2 (Critical)**

PHP 를 안 쓰니까 상관없다고 생각할 수 있지만,
워드프레스 , 드루팔 , 줌라 같은 CMS 가 전부 PHP 기반이다.
서버 언어가 알려진 웹사이트의 약 69% 가 PHP 를 쓰고 있으니, 사실상 인터넷 절반 이상이 대상인 셈이다.

---

## 용어부터 정리

### RCE (Remote Code Execution)

원격 코드 실행
공격자가 내 서버에 **자기가 원하는 코드를 실행**시킬 수 있다는 뜻
코드 실행이 되면 파일 탈취 , 악성코드 설치 , 다른 서버로 이동까지 다 가능하다.

여기에 **인증 없이 (Unauthenticated)** 가 붙으면, 로그인도 필요 없이 요청만 보내면 된다는 뜻이다.

### Use-After-Free (UAF)

이미 해제한 메모리를 **다시 사용하는** 버그

```
1. 메모리 할당 → 데이터 저장
2. 다 썼으니 메모리 해제 (free)
3. 그런데 어딘가에 아직 그 주소가 남아있음
4. 남은 주소로 다시 접근 (use) → 그 자리에 공격자가 넣은 데이터가 있다면?
```

죽은 줄 알았던 메모리가 **좀비처럼 살아 돌아오는** 버그다.
공격자는 그 빈자리에 자기 데이터를 심어서 프로그램 흐름을 가로챈다.

---

## 무엇이 문제였나

두 취약점 모두 PHP **엔진 자체**의 메모리 버그다.
그래서 내가 짠 코드가 아무리 깔끔해도, PHP 버전이 취약하면 그대로 노출된다.

### CVE-2026-109618 : 메모리 부족 (OOM) 처리 중 메모리 손상

- PHP 는 메모리 할당에 실패하면 요청 처리를 중간에 포기한다
- 이때 **반쯤 만들어진 요청 데이터**가 정리(cleanup) 단계에서 사용된다
- 공격자는 조작한 multipart 요청 (파일 업로드 형식의 요청) 으로 이 상황을 일부러 만든다
- 설정된 크기 제한 안에서도 발생 가능

Apache mod_php 환경이 특히 위험하다.
**애플리케이션 코드가 실행되기도 전에** 터질 수 있기 때문이다.

### CVE-2026-109619 : 요청 사이에 남은 오래된 상태

이건 PHP 서버 구조를 알아야 이해가 쉽다.

```
PHP-FPM / mod_php 는 워커 프로세스를 재사용한다

[워커 1] 요청 A 처리 → 끝 → 요청 B 처리 → 끝 → 요청 C 처리 ...
```

- 요청 A 가 치명적 에러나 타임아웃으로 **정리되지 못하고 끊긴다**
- 내부 상태가 요청 A 에서 이미 해제된 메모리를 계속 가리킨다
- 같은 워커가 다음 요청 B 를 처리할 때 그 값을 다시 쓴다 → Use-After-Free

주요 경로는 **세션 업로드 진행률 (session upload progress)** 기능인데, 이게 **기본값으로 켜져 있다.**

참고로 에러를 숨기는 건 소용없다.
error_reporting 을 낮추거나 @ 연산자 , display_errors 를 꺼도 막히지 않는다.

---

## 영향 범위

| 브랜치 | 취약 | 패치 버전 |
|---|---|---|
| PHP 8.5 | 8.5.12 미만 | **8.5.12** |
| PHP 8.4 | 8.4.27 미만 | **8.4.27** |
| PHP 8.3 | 8.3.36 미만 | **8.3.36** |
| PHP 8.2 | 8.2.35 미만 | **8.2.35** (지원 종료 2026-12-31) |
| PHP 8.1 이하 | 지원 종료 | 공식 바이너리 없음 → 지원 버전으로 업그레이드 |

PHP 5.4 이후 거의 모든 버전이 최소 하나에 해당된다.
PHP-FPM , mod_php , php-cgi , FrankenPHP , LiteSpeed 모두 영향을 받는다.

(8.1 이하는 7.4 , 8.0 , 8.1 용 소스 패치만 나왔고 바이너리는 없다)

---

## 그래서 뭘 해야 하나

### 1. 버전 확인

```bash
php -v        # CLI 버전
php-fpm -v    # FPM 버전
```

CLI 버전과 실제 웹에서 돌아가는 버전이 **다를 수 있다.** 웹 서버 쪽 버전을 꼭 따로 확인하자.

### 2. 패치 + 워커 재시작

패치 버전으로 올리는 게 **유일한 완전한 해결책**이다.
그리고 반드시 워커를 재시작해야 적용된다.

```bash
# PHP-FPM
sudo systemctl restart php-fpm

# mod_php (Apache)
sudo systemctl restart apache2   # 또는 httpd
```

재시작을 안 하면 기존 워커가 옛날 코드로 계속 돌아간다.

### 3. 당장 패치가 어렵다면 (임시 완화)

완전한 해결책은 아니고, 노출을 줄이는 용도다.

```ini
; php.ini 또는 FPM pool 설정 (ini_set() , .user.ini 로는 늦어서 효과 없음)
session.upload_progress.enabled = 0

; PHP 8.5 만
fatal_error_backtraces = 0

; 업로드가 필요 없으면 8M , 필요하면 32M
post_max_size = 8M
```

- 설정 변경 후에도 **워커 재시작** 필요
- 웹 서버 / 프록시에서 요청 크기 , 헤더 수를 제한하고, 안 쓰는 곳은 multipart 요청 자체를 막는다
- WAF (웹 방화벽) 도 어느 정도 도움이 된다
- 국내 호스팅 (카페24 등) 은 session.upload_progress.enabled 를 Off 로 선제 적용하기도 했다

---

## 실제 공격은 있었나 ?

기관마다 말이 다르다.

- CISA (미국 사이버보안청) : 공개 시점 기준 실제 악용은 확인 안 됨
- Amazon : 공개 4일 전인 10월 17일에 이미 공격 시도를 탐지
- watchTowr , Cloudflare : 실제 악용을 관측했다고 발표
- Rapid7 : 공개 PoC 가 여러 개 있지만 특정 OS / 버전 / 웹 서버 조합에서만 동작

정리하면 **아직 만능 공격 코드는 없지만, 시도는 계속 늘고 있다.**
언제 범용 공격 코드가 나올지 모르니 미루지 않는 게 답이다.

---

## AI 가 찾은 취약점

이번 이슈에서 개인적으로 제일 흥미로운 부분

- Wiz 연구팀은 Gemini 4 Argon , GPT-5.6 Sol 같은 AI 모델을 써서 취약점을 찾고, 공격 코드 개발과 패치 검증까지 했다
- Calif 의 연구원도 OpenAI 의 "Patch the Planet" 프로젝트에서 GPT-5.6 Sol 로 같은 취약점을 독립적으로 찾았다
- 그중 메모리 부족 문제는 2024년에 PHP 코어 개발자가 이미 발견했지만, 수정 방법에 합의하지 못해 그대로 남아 있었다고 한다

AI 가 코드를 짜주는 걸 넘어서, **10년 넘게 숨어 있던 엔진 버그**를 찾아내는 시대가 됐다.

(AI 가 외부 도구와 연결되는 방식이 궁금하다면 [MCP (Model Context Protocol)](https://problem-child.tistory.com/125) 글도 참고해 주세요)

---

## 타임라인

| 날짜 | 내용 |
|---|---|
| 2024 | PHP 코어 개발자가 OOM 문제 발견 , 수정 합의 실패 |
| 2026-08 | Calif , Wiz 가 각각 AI 로 취약점 발견 |
| 2026-08-24 | Wiz 가 PHP 보안팀에 제보 |
| 2026-10-17 | Amazon , 공개 전 공격 시도 탐지 |
| 2026-10-20 | PHP 가 취약점 존재를 사전 공지 |
| 2026-10-21 | 패치 버전 배포 + 상세 공개 , CISA 긴급 경보 |

---

## 정리

- PHP 엔진 자체의 메모리 버그라 **코드를 잘 짜도 막을 수 없다**
- 해결책은 **8.5.12 / 8.4.27 / 8.3.36 / 8.2.35 로 패치 + 워커 재시작**
- 8.1 이하는 지원 종료 버전이라 이참에 업그레이드
- 임시로는 session.upload_progress.enabled = 0 , 요청 크기 제한

PHP 를 직접 안 쓰더라도 회사 홈페이지나 블로그가 워드프레스라면 한 번 확인해 보자.

---

### 참고

- [CISA - Critical Vulnerabilities in PHP Require Immediate Patching](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)
- [Wiz - PHP2Shell](https://www.wiz.io/blog/php2shell-php-rce)
- [Rapid7 - CVE-2026-109618 and CVE-2026-109619](https://www.rapid7.com/blog/post/etr-cve-2026-109618-and-cve-2026-109619-critical-unauthenticated-remote-code-execution-in-php/)
- [지니언스 - PHP 원격 코드 실행 취약점 긴급 안내](https://www.genians.co.kr/blog/threat_intelligence/php)
- [카페24 - PHP 긴급 보안 취약점 조치 공지](https://help.cafe24.com/notice/system-notice/20261021_php-security-emergency/)
