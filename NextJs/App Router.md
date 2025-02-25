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


