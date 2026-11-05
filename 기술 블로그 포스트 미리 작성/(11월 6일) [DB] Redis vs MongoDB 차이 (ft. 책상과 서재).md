## 둘 다 NoSQL 인데 ?

채용 공고를 보면 Redis 와 MongoDB 가 나란히 적혀 있다.
둘 다 NoSQL 이니까 비슷한 DB 처럼 보이지만, 사실 **쓰임새가 꽤 다르다.**

책상과 서재로 생각하면 쉽다.

- **Redis** : 책상 위. 손만 뻗으면 바로 닿지만 **공간이 좁다**
- **MongoDB** : 서재. 찾는 데 조금 더 걸리지만 **많이 보관하고 , 목차로 찾을 수 있다**

(SQL 이 뭔지 먼저 보고 싶다면 [SQL 이란](https://problem-child.tistory.com/71) 글을 참고해 주세요)

---

## NoSQL 이란

**Not Only SQL** 의 줄임말이다.
SQL 을 안 쓴다는 뜻이라기보다, 테이블과 행으로 이루어진 **관계형 모델이 아닌 DB** 를 묶어서 부르는 말이다.

| 종류 | 저장 방식 | 예시 |
|---|---|---|
| 키-값 (Key-Value) | 키 하나에 값 하나 | **Redis** , DynamoDB |
| 문서 (Document) | JSON 같은 문서 | **MongoDB** , Couchbase |
| 컬럼 패밀리 (Column Family) | 행마다 다른 컬럼 묶음 | Cassandra , HBase |
| 그래프 (Graph) | 노드와 관계 | Neo4j |

같은 NoSQL 이어도 Redis 와 MongoDB 는 **종류부터 다르다.**

---

## Redis : 책상 위

**Remote Dictionary Server** 의 줄임말
데이터를 **메모리 (RAM)** 에 두고, **키로 값을 찾는** 저장소다.

```bash
SET user:1:name "철수"
GET user:1:name          # "철수"

EXPIRE user:1:name 60    # 60초 뒤 자동 삭제
TTL user:1:name          # 남은 시간 확인
```

### 값으로 자료구조를 쓸 수 있다

문자열만 넣는 게 아니라, 값 자체가 자료구조다.

| 타입 | 설명 | 쓰임새 |
|---|---|---|
| String | 문자열 , 숫자 | 캐시 , 카운터 |
| Hash | 필드-값 묶음 | 객체 저장 |
| List | 순서 있는 목록 | 간단한 큐 |
| Set | 중복 없는 집합 | 좋아요 누른 사람 |
| Sorted Set | 점수로 정렬된 집합 | 랭킹 |

랭킹을 만들면 이렇게 된다.

```bash
ZADD ranking 100 "철수" 300 "영희" 200 "민수"

ZRANGE ranking 0 2 REV WITHSCORES   # 점수 높은 순으로 3명
```

정렬을 직접 짤 필요 없이, 넣기만 하면 Redis 가 순서를 유지한다.

### 왜 빠를까

- 디스크가 아니라 **메모리**에서 읽고 쓴다
- 명령을 **한 번에 하나씩** 처리한다 (명령 실행은 싱글 스레드)

자바스크립트와 비슷한 구조다.
(혼자서 어떻게 빠르게 처리하는지는 [이벤트 루프](https://problem-child.tistory.com/129) 글이 비슷한 이야기입니다)

한 번에 하나씩 실행하니까 `INCR` 같은 명령이 중간에 끼어들 일이 없다.
대신 전체 키를 훑는 `KEYS *` 같은 **오래 걸리는 명령 하나가 전체를 멈출 수 있다.** 운영에서는 `SCAN` 을 쓰자.

### 메모리에 있으면 꺼지면 날아가나 ?

설정하기 나름이다. Redis 는 디스크에 저장하는 방법을 두 가지 제공한다.

- **RDB** : 일정 시점의 메모리를 통째로 찍어두는 스냅샷
- **AOF** : 실행한 쓰기 명령을 파일에 계속 기록

그래도 AOF 를 1초마다 저장하는 일반적인 설정이면 **장애 시 최근 데이터가 조금 사라질 수 있다.**
그래서 잃으면 안 되는 원본 데이터는 보통 다른 DB 에 둔다.

### 메모리가 꽉 차면 ?

책상이 꽉 찬 상황이다.
`maxmemory` 로 한도를 정하고, 넘치면 어떻게 할지 정책을 고른다.

| 정책 | 동작 |
|---|---|
| noeviction (기본값) | 지우지 않고 쓰기를 에러로 거절 |
| allkeys-lru | 오래 안 쓴 키부터 삭제 |
| volatile-ttl | TTL 이 있는 키 중 만료가 가까운 것부터 삭제 |

메모리는 디스크보다 비싸다.
**큰 데이터를 전부 Redis 에 넣으면 비용이 크게 늘어난다.** 책상을 서재만큼 키우는 셈이다.

---

## MongoDB : 서재

데이터를 **BSON** (JSON 을 바이너리로 바꾼 형식) **문서**로 **디스크**에 저장하는 DB 다.
자주 쓰는 데이터는 메모리에 캐시해 둔다.

SQL 과 용어를 맞춰 보면

| SQL | MongoDB |
|---|---|
| 테이블 (Table) | 컬렉션 (Collection) |
| 행 (Row) | 문서 (Document) |
| 컬럼 (Column) | 필드 (Field) |
| JOIN | $lookup 또는 문서 안에 포함 |

```javascript
db.posts.insertOne({
  title: "Redis vs MongoDB",
  author: { name: "철수", job: "개발자" },  // 객체를 그대로
  tags: ["redis", "mongodb"],               // 배열도 그대로
  views: 120,
});
```

### 스키마가 유연하다

테이블처럼 컬럼을 미리 정하지 않아도 된다.
같은 컬렉션에 필드가 다른 문서를 넣을 수 있다.

```javascript
db.posts.insertOne({ title: "글 1", views: 10 });
db.posts.insertOne({ title: "글 2", thumbnail: "cat.png" });  // views 없음 , 그래도 OK
```

게시글과 태그처럼 SQL 이라면 테이블을 나눌 데이터를 **한 문서에 같이** 담을 수 있다.
함께 읽는 데이터면 JOIN 없이 한 번에 가져오는 장점이 있다.

대신 자유로운 만큼, 잘못된 형식이 들어가지 않게 **애플리케이션이나 스키마 검증으로 관리**해야 한다.

### 값으로 검색할 수 있다

Redis 와 제일 크게 갈리는 부분이다.

```javascript
// redis 태그가 있고 조회수 100 이상인 글을 조회수 순으로
db.posts
  .find({ tags: "redis", views: { $gte: 100 } })
  .sort({ views: -1 })
  .limit(5);
```

Redis 는 기본적으로 **키를 알아야** 값을 꺼낸다.
MongoDB 는 **문서 안의 어떤 필드로든** 찾을 수 있고, 인덱스를 걸면 빨라진다.

```javascript
db.posts.createIndex({ tags: 1, views: -1 });
```

(인덱스가 왜 빠르고 왜 과하면 독인지는 [Index 란 ?](https://problem-child.tistory.com/122) 글을 참고해 주세요)

### 집계도 된다

SQL 의 GROUP BY 처럼 , 저장된 데이터로 통계를 낼 수 있다.

```javascript
// 태그별 글 개수
db.posts.aggregate([
  { $unwind: "$tags" },                          // 배열을 한 줄씩 펼치고
  { $group: { _id: "$tags", count: { $sum: 1 } } },  // 태그별로 묶어서 세고
  { $sort: { count: -1 } },                      // 많은 순으로
]);
```

### 알아둘 제한

- 문서 하나의 최대 크기는 **16MB**
- 문서 하나의 쓰기는 원자적이다. 여러 문서를 묶는 **트랜잭션도 지원**하지만, 레플리카 셋 이상의 구성이 필요하다

---

## 어떤 데이터를 어디에 ?

| 데이터 | 어울리는 곳 | 이유 |
|---|---|---|
| 자주 읽는 조회 결과 (캐시) | Redis | 빠르고 , TTL 로 자동 삭제 |
| 로그인 세션 , 인증 토큰 | Redis | 키로 찾고 , 만료가 필요 |
| 실시간 랭킹 , 카운터 | Redis | Sorted Set , INCR |
| 분산 락 | Redis | `SET key value NX EX 10` |
| 게시글 , 상품 , 프로필 | MongoDB | 구조가 다양하고 영구 보관 |
| 로그 , 이벤트 기록 | MongoDB | 양이 많고 필드가 자주 바뀜 |
| 조건 검색 , 통계 | MongoDB | 쿼리 , 인덱스 , 집계 |

판단 기준은 두 개면 충분하다.

- **키만 알면 되고 , 사라져도 다시 만들 수 있다** → Redis
- **조건으로 찾아야 하고 , 사라지면 안 된다** → MongoDB

### 대시보드 데이터를 Redis 에 넣어도 될까 ?

원본 데이터가 많으면 전부 Redis 에 넣는 건 어울리지 않는다.
메모리 비용도 크고, 조건 검색과 집계도 불편하다.

원본은 MongoDB 같은 DB 에 두고,
**이미 계산한 집계 결과만 TTL 을 걸어 Redis 에 캐싱**하는 쪽이 자연스럽다.

---

## 같이 쓰는 경우가 많다

둘은 경쟁 관계라기보다, **역할이 달라서 같이 쓴다.**
대표적인 패턴이 **Cache-Aside** 다.

```
1. Redis 에 있나 확인        → 있으면 바로 반환 (캐시 히트)
2. 없으면 MongoDB 에서 조회   (캐시 미스)
3. Redis 에 저장 (TTL 포함)
4. 반환
```

```javascript
async function getPost(id) {
  const key = `post:${id}`;

  const cached = await redis.get(key);
  if (cached) return JSON.parse(cached);

  const post = await db.collection("posts").findOne({ _id: id });
  await redis.set(key, JSON.stringify(post), { EX: 60 });  // 60초 캐싱

  return post;
}
```

자주 보는 책은 책상에 꺼내 두고, 없으면 서재에 가서 가져오는 것과 같다.

원본이 바뀌면 캐시와 값이 달라질 수 있다.
그래서 수정할 때 캐시를 지우거나, TTL 을 짧게 잡아서 **언젠가는 맞춰지도록** 한다.

---

## Redis vs MongoDB

| 항목 | Redis | MongoDB |
|---|---|---|
| 종류 | 키-값 저장소 | 문서 DB |
| 주 저장 위치 | 메모리 | 디스크 (일부 메모리 캐시) |
| 데이터 형태 | String , Hash , List , Set , Sorted Set 등 | BSON 문서 |
| 조회 방식 | 기본적으로 키로 조회 | 필드 조건 쿼리 , 집계 |
| 인덱스 | 키 기반 (별도 구조는 직접 설계) | 필드별 보조 인덱스 |
| 저장 용량 | 메모리 크기가 한계 | 디스크 크기만큼 , 샤딩으로 확장 |
| 속도 | 매우 빠름 | 빠름 (Redis 보다는 느림) |
| 영속성 | 선택 (RDB , AOF) | 기본 |
| 데이터 만료 | 키마다 TTL | TTL 인덱스 |
| 주 용도 | 캐시 , 세션 , 랭킹 , 분산 락 | 서비스 주 데이터 저장 |
| 비유 | 책상 위 | 서재 |

---

## 정리

- 둘 다 NoSQL 이지만 Redis 는 **키-값** , MongoDB 는 **문서** DB 다
- **Redis** 는 메모리에 둬서 빠르다 → 캐시 , 세션 , 랭킹처럼 키로 찾는 데이터에 좋다
- **MongoDB** 는 디스크에 문서로 저장한다 → 조건 검색과 집계가 필요한 주 데이터에 좋다
- Redis 는 메모리가 비싸니 **큰 원본 데이터를 전부 넣는 용도가 아니다**
- 실제로는 MongoDB 를 원본으로 , Redis 를 캐시로 **같이** 쓰는 구조가 흔하다

자주 쓰는 건 책상에, 오래 둘 건 서재에.
