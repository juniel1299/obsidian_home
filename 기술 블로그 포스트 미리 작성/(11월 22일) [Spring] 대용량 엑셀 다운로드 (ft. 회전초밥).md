## 엑셀 다운로드 눌렀더니 서버가 죽었다

관리자 화면에 꼭 있는 기능이 **엑셀 다운로드**다.
데이터가 적을 때는 아무 문제가 없다.
그런데 몇십만 건이 되면 버튼 한 번에 이런 에러가 난다.

```
java.lang.OutOfMemoryError: Java heap space
```

한 명의 다운로드 때문에 **서버 전체가 멈출 수도 있다.**

회전초밥으로 생각하면 쉽다.

- **한 번에 다 만들기** : 주문받은 초밥 1만 접시를 다 만들어서 테이블에 쌓는다 → 테이블이 무너진다
- **회전초밥** : 몇 접시씩 만들어서 레일로 계속 흘려보낸다 → 테이블에는 늘 몇 접시만 있다

이번 글은 Spring + Apache POI 로 대용량 엑셀을 **회전초밥처럼** 만드는 방법을 정리한다.

---

## 메모리가 터지는 곳은 두 군데

```java
// ❌ 흔한 첫 구현
List<Order> orders = orderMapper.findAll();         // ① 전체 조회

Workbook wb = new XSSFWorkbook();                    // ② 전체를 메모리에 만듦
Sheet sheet = wb.createSheet("주문");
for (int i = 0; i < orders.size(); i++) {
    Row row = sheet.createRow(i);
    row.createCell(0).setCellValue(orders.get(i).getId());
    // ...
}
wb.write(response.getOutputStream());
```

- **① 조회 결과** : 30만 건을 `List` 하나에 다 담는다
- **② 엑셀 객체** : `XSSFWorkbook` 은 모든 행 , 모든 셀을 **객체로 메모리에 들고 있다**

둘 다 데이터가 늘어나는 만큼 메모리를 쓴다.
테이블 하나에 초밥을 계속 쌓는 구조다.

---

## 직접 비교해 봤다

조건

- Apache POI 5.4.1
- 힙 메모리 256MB (`-Xmx256m`)
- 한 행에 문자열 셀 10개

| 방식 | 행 수 | 결과 |
|---|---|---|
| XSSFWorkbook | 10,000 | 성공 |
| XSSFWorkbook | 20,000 | **OutOfMemoryError** |
| SXSSFWorkbook | 300,000 | 성공 (약 3초) |
| SXSSFWorkbook | 1,000,000 | 성공 (약 6.7초) |

`XSSFWorkbook` 은 **2만 행**에서 이미 터졌다.
`SXSSFWorkbook` 은 같은 메모리로 **100만 행**까지 만들었다.

(숫자는 셀 내용 , 서버 사양에 따라 달라진다. 차이의 크기를 보면 된다)

---

## 해결 1 : SXSSFWorkbook (엑셀을 흘려보내기)

POI 에는 엑셀을 만드는 방식이 세 가지 있다.

| 클래스 | 형식 | 특징 |
|---|---|---|
| HSSFWorkbook | .xls (옛날 형식) | 시트당 65,536행 제한 |
| XSSFWorkbook | .xlsx | 모든 행을 메모리에 보관 |
| **SXSSFWorkbook** | .xlsx | **일정 행만 메모리에 , 나머지는 임시 파일로** |

```java
try (SXSSFWorkbook wb = new SXSSFWorkbook(100)) {  // 메모리에는 최근 100행만
    Sheet sheet = wb.createSheet("주문");

    for (int i = 0; i < 1_000_000; i++) {
        Row row = sheet.createRow(i);
        row.createCell(0).setCellValue("값 " + i);
    }

    wb.write(response.getOutputStream());
}  // close() 할 때 임시 파일도 정리된다
```

`new SXSSFWorkbook(100)` 의 100 이 **레일 위 접시 수**다.
101번째 행을 만드는 순간 , 가장 오래된 행은 **디스크의 임시 파일로 내려간다.**

### 알아둘 제약

흘려보낸 초밥은 다시 집을 수 없다.

- 이미 내려간 행은 **다시 읽거나 수정할 수 없다** (`sheet.getRow()` 가 null)
- `autoSizeColumn()` 은 메모리에 남은 행만 보고 계산한다. 열 너비는 `sheet.setColumnWidth()` 로 **직접 정하는 게** 낫다
- 임시 파일이 디스크를 쓰니 **서버 디스크 여유**도 확인해야 한다 (`wb.setCompressTempFiles(true)` 로 줄일 수 있다)

참고로 POI 5.4 에서는 예전에 쓰던 `wb.dispose()` 가 deprecated 됐다.
try-with-resources 로 `close()` 하면 임시 파일까지 정리된다.

---

## 해결 2 : 조회도 나눠서 (초밥 재료도 조금씩)

엑셀을 흘려보내도 , 조회를 한 번에 다 하면 ① 에서 터진다.
그래서 **일정 건수씩 끊어서 조회하고 , 쓴 다음 , 다음 묶음을 조회**한다.

### OFFSET 보다 마지막 ID 기준으로

```sql
-- ❌ OFFSET 방식 : 뒤로 갈수록 느려진다
SELECT * FROM orders ORDER BY id
OFFSET 900000 ROWS FETCH NEXT 5000 ROWS ONLY;

-- ✅ 마지막 ID 기준 (키셋 페이징)
SELECT * FROM orders
WHERE id > #{lastId}
ORDER BY id
FETCH FIRST #{size} ROWS ONLY;
```

OFFSET 900000 은 앞의 90만 건을 **읽고 버린 뒤** 5000건을 가져온다.
묶음이 뒤로 갈수록 점점 느려진다.

마지막 ID 기준은 인덱스로 **바로 그 위치부터** 읽는다.
다운로드 도중 데이터가 추가 / 삭제돼도 **중복되거나 빠지는 행이 없다** 는 장점도 있다.

(인덱스가 왜 빠른지는 [Index 란 ?](https://problem-child.tistory.com/122) 글을 참고해 주세요)

### 묶음 크기는 절충

| 묶음 크기 | 메모리 | 조회 횟수 |
|---|---|---|
| 작게 (500) | 적게 씀 | 많아짐 → 느려짐 |
| 크게 (50,000) | 많이 씀 | 적어짐 |

보통 수천 건 단위에서 시작해서 , 메모리와 속도를 **측정하며** 정한다.

(MyBatis 의 `ResultHandler` , JDBC `fetchSize` 처럼 한 번의 조회 결과를 **한 줄씩 받아오는** 스트리밍 조회 방법도 있다)

---

## 합치면 : Controller

```java
@GetMapping("/orders/excel")
public void downloadOrders(HttpServletResponse response) throws IOException {
    String fileName = URLEncoder.encode("주문목록.xlsx", StandardCharsets.UTF_8)
            .replace("+", "%20");
    response.setContentType(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    response.setHeader("Content-Disposition",
            "attachment; filename*=UTF-8''" + fileName);  // 한글 파일명

    try (SXSSFWorkbook wb = new SXSSFWorkbook(100)) {
        Sheet sheet = wb.createSheet("주문");
        writeHeader(sheet);

        int rowNum = 1;
        long lastId = 0;
        List<Order> chunk;

        while (!(chunk = orderMapper.findAfter(lastId, CHUNK_SIZE)).isEmpty()) {
            for (Order order : chunk) {
                Row row = sheet.createRow(rowNum++);
                row.createCell(0).setCellValue(order.getId());
                row.createCell(1).setCellValue(order.getCustomerName());
                row.createCell(2).setCellValue(order.getTotal().doubleValue());
            }
            lastId = chunk.get(chunk.size() - 1).getId();
        }

        wb.write(response.getOutputStream());
    }
}
```

- 조회 : `CHUNK_SIZE` 건씩
- 엑셀 : 메모리에는 100행씩
- 메모리에 올라가는 양이 **전체 건수와 상관없이 일정**해진다

레일 위에는 늘 몇 접시만 있고 , 손님은 끝없이 받아 갈 수 있다.

---

## 해결 3 : 너무 크면 비동기로

100만 건을 만드는 데 몇십 초가 걸리면 , 다른 문제가 생긴다.

- 로드밸런서 , 프록시의 **타임아웃** (AWS ALB , Nginx 모두 기본 60초) 에 걸려 연결이 끊긴다
- 사용자가 기다리다 **버튼을 또 누른다** → 같은 작업이 여러 번 돈다

그래서 아주 큰 다운로드는 **주문과 수령을 나눈다.**

```
1. 사용자 : "엑셀 만들어 주세요"     → 서버 : 작업 번호 발급 (바로 응답)
2. 서버   : 백그라운드에서 파일 생성 → 파일 저장소 (S3 등) 에 저장
3. 사용자 : 진행 상태 확인 (폴링 , 알림)
4. 완료   : 다운로드 링크 제공 (만료 시간 있는 링크)
```

진동벨을 받고 자리에서 기다리는 카페 주문과 같다.
같은 사용자의 작업이 이미 돌고 있으면 **새 요청을 막는** 처리도 같이 해 두자.

---

## 그 밖에 챙길 것

### 엑셀 자체의 한계

`.xlsx` 시트 하나에는 **1,048,576 행**까지만 들어간다.
그 이상이면 시트를 나누거나 , CSV 로 내려준다.

### CSV 도 선택지

| | XLSX | CSV |
|---|---|---|
| 서식 , 여러 시트 | 가능 | 불가 |
| 만드는 비용 | 무거움 | 가벼움 (그냥 텍스트) |
| 행 제한 | 시트당 약 104만 | 없음 (엑셀로 열 때는 제한 있음) |

CSV 를 엑셀로 열 때 한글이 깨지면 , 파일 맨 앞에 **UTF-8 BOM** (`﻿`) 을 붙인다.

### 프론트에서 받을 때

```javascript
// 파일 전체를 브라우저 메모리에 올린 뒤 저장한다
const res = await axios.get("/orders/excel", { responseType: "blob" });
```

`blob` 으로 받으면 다운로드가 끝날 때까지 **파일 전체가 브라우저 메모리**에 있다.
큰 파일은 `<a href="/orders/excel">` 처럼 **브라우저가 직접 받게** 하는 편이 낫다.
(토큰을 헤더로 보내야 하는 구조라면 , 위의 만료 시간 있는 다운로드 링크 방식이 잘 맞는다)

### 권한과 개인정보

엑셀 다운로드는 **데이터를 통째로 밖으로 꺼내는 기능**이다.

- 다운로드 권한을 화면 조회 권한과 **따로** 관리한다
- 누가 언제 무엇을 받았는지 **기록**을 남긴다
- 필요 없는 개인정보 컬럼은 **마스킹**하거나 뺀다

---

## 방식 비교

| 항목 | 한 번에 (XSSF + 전체 조회) | 스트리밍 (SXSSF + 나눠 조회) | 비동기 생성 |
|---|---|---|---|
| 메모리 | 데이터만큼 증가 | 일정 | 일정 |
| 구현 난이도 | 쉬움 | 보통 | 어려움 (작업 관리 , 저장소) |
| 응답 | 바로 다운로드 | 바로 다운로드 | 나중에 링크로 |
| 타임아웃 위험 | 있음 | 데이터가 아주 크면 있음 | 없음 |
| 서식 , 셀 수정 | 자유로움 | 이미 내려간 행은 불가 | 방식에 따라 다름 |
| 어울리는 양 | 수천 건 | 수만 ~ 수십만 건 | 수십만 건 이상 , 오래 걸리는 작업 |
| 비유 | 테이블에 다 쌓기 | 회전초밥 레일 | 진동벨 주문 |

---

## 정리

- 대용량 엑셀에서 메모리는 **조회 결과**와 **엑셀 객체** 두 군데서 터진다
- `XSSFWorkbook` 은 모든 행을 메모리에 든다. **`SXSSFWorkbook`** 은 일정 행만 남기고 디스크로 내린다
- 조회도 **키셋 페이징**으로 나눠서 , 조회 → 쓰기 → 다음 묶음 순으로
- 그러면 메모리가 **전체 건수와 상관없이 일정**해진다
- 아주 크면 **비동기 생성 + 다운로드 링크**로 타임아웃을 피한다
- 다운로드는 데이터를 밖으로 꺼내는 기능이니 **권한 , 기록 , 마스킹**을 챙긴다

테이블에 다 쌓지 말고 , 레일로 흘려보내자.
