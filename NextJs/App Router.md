# App Router (앱 라우터)
1. Page Router 와 달리 페이지 라우팅 설정 방식 변경됨
2. React 18 신규 기능 추가
3. 데이터 페칭 방식 변경
4. 레이아웃 설정 방식 변경
5. 페이지 라우팅 설정 방식 변경

네이게이팅 , 프리페칭 , 사전 렌더링 부분은 기존 페이지 라우터와 동일 ( 변경사항이 없음. )

파일명이 page 면 페이지 역할 , layout이면 layout 역할 

## 페이지 라우팅 
Page Router 에선 pages 폴더 아래에서 ~/search -> search.tsx 파일 식이지만
App Router 에선 app 폴더 아래에서 /search 폴더 아래의 page.tsx 로 작성해야 동일한 동작이 가능함. 

동적 경로의 경우
App Router는 \[id\] 폴더 아래에 page.tsx 작성하면 됨 -> book/1 , book/2 등등 .

### 페이지 라우팅 설정 
폴더명이 경로 화면은 page.tsx 로 꾸민다 .

폴더명/\[id\] -> book/id 에 해당하는 화면 ex)book/1 , book/100
폴더명/\[...id\] -> 해당 화면 뒤에 추가적으로 이어 붙일 수 있음 ex) book/1/2/3/4/5
폴더명/\[\[id\]\] -> /book 뒤에 추가 경로가 없는 경우 ex) /book

### 레이아웃 설정
폴더명이 경로 화면의 레이아웃은 layout.tsx 로 작성함 
ex ) book 폴더에 layout.tsx로 레이아웃 파일 작성 -> 하위에 폴더를 만들어도 상위 layout.tsx 적용받음.
만약 하위에는 새로운 layout을 적용하고 싶으면 하위 폴더에 layout.tsx 작성 -> 2개가 중첩으로 적용됨.

설정을 따로 하지 않으면 레이아웃 파일을 작성하면 기존 page.tsx에 있던건 화면에 뜨지 않음

```typeScript
import { ReactNode } from "react";

export default function Layout({children}:{children:ReactNode}){

	return(
	
		<div>
		
			<div>임시 서치바</div>
			
			{children}
		
		</div>
	
	)

}
```

이렇게 불러오는 방법이 있음. 

#### 라우트 그룹
폴더명을 (with-searchbar) 로 작성해야함 
경로상에는 아무런 영향을 주지 않음 (소괄호로 감싸면)


## React Server Component (리액트 서버 컴포넌트)

해당 기능이 없을땐 필요한 컴포넌트 필요없는 컴포넌트 구분 없이 JS Bundle에 그냥 다 묶어서 전달해버림
-> JS Bundle 용량이 너무 커져버림 ..

해당 기능의 경우 필요한 컴포넌트만 JS Bundle 에 담아서 전달함 
-> JS Bundle 용량이 작음 . 

서버측에서만 실행되는 컴포넌트 (브라우저 실행x) 에 대해선 서버 컴포넌트로 분류 
서버 , 브라우저 똑같이 1번씩 실행되어야 할 경우 클라이언트 컴포넌트로 분류

JS Bundle 에 클라이언트 컴포넌트만 포함하여 동작

서버 컴포넌트 : 서버측에서 사전 렌더링을 진행할 때 딱 1번만 실행 
클라이언트 컴포넌트 : 사전 렌더링 진행할 때 한번, 하이드레이션 진행 시 한번 총 2번 실행

그러므로 페이지 대부분을 서버 컴포넌트로 구성하고 
클라이언트 컴포넌트 꼭 필요한 경우에만 사용 ;; 

서버 컴포넌트를 클라이언트 컴포넌트로 설정하기 위해선 최상단에 'use client'; 작성해야함 . 

```typeScript
"use client"

import { useEffect } from "react";

import style from "./page.module.css"

export default function Home() {
	console.log('Home 컴포넌트 실행');
	
	  
	
	useEffect(()=> {});
	
	const secretKey = 'ㄱㄴㄷㄹ';
	
	  
	
	return (
	
		<div className={style.page}>
		
			최상단
		
		</div>
	
	);

}
```

1. 서버 컴포넌트의 경우 브라우저에서 실행될 코드가 포함되면 안된다 . 
2. 클라이언트 컴포넌트는 클라이언트에서만 실행되지 않는다. (서버는 서버만 , 클라이언트는 둘 다)
3. 클라이언트 컴포넌트에서 서버 컴포넌트를 import 할 수 없다 (서버 컴포넌트를 클라이언트로 바꿈)
4. 서버 컴포넌트에서 클라이언트 컴포넌트에게 직렬화 되지 않는 Props는 전달 불가하다.
**((JPA 직렬화와 비슷)  객체, 배열, 클래스 등의 복잡한 구조의 데이터를 네트워크 상으로 전송하기 위해 단순한 형태로 변환하는 것)**

ex 
```typeScript
const person = {
	name : 'ㄱㄴㄷ',
	age : 10,
};


{"name":"ㄱㄴㄷ","age":27}
```
위의 형태를 아래로 바꿈 . 
단, 함수는 직렬화가 불가능하다..
### RSC Payload 
React Server Component의 순수한 데이터(결과물)
React Server Component를 직렬화 한 결과를 의미 . 

Rsc Payload 에는 서버 컴포넌트의 모든 데이터가 포함됨 
1. 서버 컴포넌트 렌더링 결과
2. 연결된 클라이언트 컴포넌트 위치
3. 클라이언트 컴포넌트에게 전달하는 Props 값 

-> 그러므로 서버 컴포넌트에서 클라이언트 컴포넌트에게 직렬화 되지 않은 Props 는 전달이 안 됨.

## Navigating (네비게이팅)
앱 라우터에선 Server Component 가 추가되면서 프리페칭 시 JS Bundle + RSC Payload 전달하게됨 
(기존엔 JS Bundle만 전달)

결국 모든 페이지를 Static , Dynamic 으로 분류 -> 대부분이 Static , 서버 렌더링 필요한 경우 Dynamic

## in App Router (데이터 페칭)

- 페이지 라우터에선 서버 컴포넌트가 최상단 컴포넌트가 되어서 서버,클라이언트단 컴포넌트 동시 동작하는 최하단 컴포넌트가 동작하기 위해 모든 컴포넌트를 다 끌고 온다는 문제가 존재 . 


- 앱 라우터에선 비동기함수를 활용하여 데이터 페칭 로직을 내부에 작성 할 수 있음. 

차이점 : 페이지 라우터에선 클라이언트 컴포넌트에 Async 를 쓸 수 없었음 
(브라우저에서 동작 시 문제를 일으킬 수 있기 때문에..)

기존에 getServerSideProps , getStaticProps 를 대체하게 됨 . 

**데이터는 필요한 곳에서 직접 불러올 수 있도록 됨**


## data cache (데이터 캐시)
fetch 메서드를 통해 불러온 데이터를 Next 서버에서 보관하는 기능 
-> 영구적으로 데이터 보관 또는 특정 시간마다 업데이트 하는 것도 가능 . 

```typeScript
const response = await fetch(`~/api`, {cache : "force-cache"});
```
요청의 결과를 무조건 캐싱 -> 한번 호출 된 이후로는 다시 호출되지 않음 . (옵션이 다양하게 존재)

```typeScript
{cache: 'no-store'} // 데이터 캐시 x 아예 캐싱을 하지 않음
{cache: 'force-cache'} // 무조건 캐싱하는 옵션 
{cache: {next: {revalidate:3} } } //특정 시간을 주기로 캐시를 업데이트함(3초) .(ISR 비슷)
```
등등 다양함.

## Request Memoization (리퀘스트 메모이제이션)
- 중복적으로 발생하는 요청들을 정리해준다. (중복된 요청을 하나로)
1. 요청 발생 -> fetch를 통해 백엔드 서버 전송 -> 화면에 적용 
2. 만약 리퀘스트 메모이제이션이 놓치면 데이터 캐시가 저장 
3. 리퀘스트 메모이제이션에 저장되면 데이터 캐시까지 가지 않음 
4. 즉 프론트 - 리퀘스트 메모이제이션 - 데이터 캐시 - 백엔드 서버  순서 

리퀘스트 메모이제이션은 하나의 페이지 렌더링 하는 동안 중복된 API 요청을 캐싱 -> 렌더링 종료시 소멸
데이터 캐시는 백엔드 서버로부터 불러온 데이터를 영구적으로 보관하기 위해 사용 (서버 가동 중에는 영구적)


서버 컴포넌트 개념이 모호해지면서 리퀘스트 메모이제이션이 필요로 해짐. 
(App Router는 각각의 컴포넌트에서 각자 데이터를 요청하기 때문에)

## Full Route Cache (풀 라우트 캐시)
Next 서버측에서 빌드 타임에 특정 페이지의 렌더링 결과를 캐싱하는 기능 


/a 페이지에 대해 사전 렌더링 - 리퀘스트 메모이제이션 - 데이터 캐시 과정을 거친 후 
해당 화면을 풀 라우트 캐시를 통해 화면을 캐싱 이후에 다시 접속 할 경우 풀 라우트 캐시 위치에서 화면을 가져옴

![[스크린샷 2025-02-26 오전 9.58.34.png]]
Next.js는 Static 과 Dynamic으로 페이지를 자동 분류함 (서버 컴포넌트에서만 유효)
**Static Page 에서만 풀 라우트 캐시가 적용됨**

Dynamic Page : 특정 페이지가 접속 요청을 받을 때 마다 매번 변화가 생기거나, 데이터가 바뀌는 경우

Dynamic Page로 설정되는 케이스 
1. 캐시되지 않는 Data Fetching을 사용 할 경우
```typeScript
async function Hello(){
	const response = await fetch("...") //또는 cache:"no-store"
	return <div></div>
}
```



