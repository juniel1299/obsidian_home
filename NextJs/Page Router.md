# 페이지 라우터
React Router 처럼 페이지 라우팅 기능을 제공함 

pages 폴더 안에 파일명 기반의 페이지 라우팅을 함 (또는 폴더)
(파일명을 우선적으로 찾은 다음 없을 경우 폴더명을 찾음)
(폴더 구조를 기반으로 페이징 라우팅을 제공함)


폴더명으로도 가능하기 때문에 폴더명을 경로로 가질 수 있음 (동적 경로)
ex : 폴더명 item , item 내의 파일명 1 , 2, 3 존재시 
\/item/1 , \/item/2 등등..


## 파일 구조 
App : 루트 컴포넌트 (리액트와 같음) , Component를 통해 화면 , Props를 통해 기능을 가져옴


## 입력 

- 쿼리형

get 방식 (q?) 쿼리 스트링을 받기 위해선 import 필요 
```javaScript
import { useRouter } from "next/router";

  

export default function Page () {

  

	const router = useRouter();
	
	  
	
	const { q } = router.query;

  

	return (

		<h1>Search{q}</h1>
	
	)

}

```
![[Pasted image 20250219133632.png]]

- 동적 경로

book 폴더 안에 파일명을 \[id\].tsx 로 적게 되면 
http://localhost:3000/book/1
이렇게 쓸 수 있으며. book/\[\] 모두에게 적용됨

```typeScript
import { useRouter } from "next/router"

  

export default function Page() {

  

	const router = useRouter();
	
	const { id } = router.query;
	
	  
	
	return (
	
		<h1>
		
			BOOK{id}
		
		</h1>
	
	)

}
```
만약 여러개의 값을 받는 경우 

파일명을 \[...id\].tsx 로 작성 시 

![[Pasted image 20250219134457.png]]

이렇게 가능 . (배열 형태로 받음 , \[999\],\[111\])

아무 값도 없는 화면을 꾸미기 위해선 index.tsx 로 하거나 \[\[book.tsx\]\]  로 작성하면 아무 값도 없을 때까지 적용 가능 . 

\[\[...book.tsx]] 하면 모두 대응 가능 . 


## 404 페이지 
app.tsx 와 같은 경로에 파일명을 404.tsx 만들면 됨 . 


## 프로그래매틱 페이지 이동 (Programmatic Navigation)
\<Link href={""} \</Link> 형식으로도 가능하지만 

```typeScript

import type { AppProps } from "next/app";
import Link from "next/link";
import { useRouter } from "next/router";

export default function App({ Component, pageProps }: AppProps) {

	const router = useRouter();
	
	const onClickButton = () => {
	
		router.push('/test');
	
	};
	
	return <>
	
		<header>
		
		<Link href={'/'}>인덱스</Link>
		
		&nbsp;
		
		<Link href={'/search'}>search</Link>
		
		&nbsp;
		
		<Link href={'/book/1'}>book/1</Link>
		
		<div>
		
			<button onClick={onClickButton}>/test 페이지로 이동</button>
		
		</div>
		
		</header>
		
		<Component {...pageProps} /> 
	</>;
}
```
이렇게 onClick을 이용해서 가능함. 
push 이외에
replace (뒤로가기 방지하며 페이지 이동)
back (뒤로 가기)
등등의 기능 존재 . 


## Pre-fetching (프리패칭)
현재 사용자가 보고 있는 화면에서 이동 할 수 있는 경우의 수를 미리 데이터를 불러놓음 . 

ex) 현재 화면에 a , b , c 라는 링크를 탈 수 있음  -> a , b , c 에 대한 화면을 미리 대기시킴


### 리액트는 JS Bundle 로 분명 다 받아온다 했는데 프리패칭이 왜 필요한가?

모든 컴포넌트는 페이지 별로 분리해서 미리 저장해놓음. -> 현재 페이지에 해당되는 JS Bundle 만 전달됨 (전체아님)

(만약 한꺼번에 컴포넌트 다 보내면 초기 용량이 너무 커져서 최초 동작이 너무 느림.)


npm run build
npm run dev

## API
처음 프로젝트 생성하면 생기는 API 폴더 내부의 hello.ts 구조와 같음 . 

```typeScript
import type { NextApiRequest, NextApiResponse } from "next";

  

export default function handler (

	req:NextApiRequest,
	
	res:NextApiResponse,

){

	const date = new Date();
	
	res.json({time:date.toLocaleString()});

}
```

next에서 제공하는 apirequest , apiresponse 를 사용하면 된다. 

## CSS 
기존 방식으로 import 불가능 . 

```typeScript
import style from './index.module.css';

export default function Home() {

	return (
	
	<>
	
	<h1 className={style.title}>
	
		인덱스
	
	</h1>
	
	<h2 className={style.h2}>
	
		h2인덱스
	
	</h2>
	
	</>
	
	);

}
```

App.tsx 파일 import 

import "@/styles/globals.css"; 처럼 next.js 는 일반적인 방식으로 import 불가능 .

css 파일명은 .module.css 로 끝나게 작성하여야한다. 

## Global Layout (글로벌 레이아웃)

헤더 , 푸터 같은 동일한 내용은 하나의 파일로 빼놓자 . 

App 파일의 컴포넌트를 GlobalLayouts 로 감싸서 헤더 , 푸터를 공유한다. 

(App 파일)
```typeScript
import GlobalLayouts from "@/components/global-layout";

import "@/styles/globals.css";

import type { AppProps } from "next/app";

  

export default function App({ Component, pageProps }: AppProps) {

return (

	<>
	
		<GlobalLayouts>
		
			<Component {...pageProps} />
		
		</GlobalLayouts>
		
	</>

);

}
```

global-layout.tsx 파일 
```typeScript
import { ReactNode } from "react";

export default function GlobalLayouts({

	children,

}:{

	children:ReactNode;

}){

	return (
	
		<>
		
		<header>헤더</header>
		
		<main>
		
			{children}
		
		</main>
		
		<footer>푸터</footer>
		
		</>
	
	);

}
```

### 페이지 별 레이아웃 설정
특정 페이지에서만 나오게 하기 위해선 내가 띄우고 싶은 화면에 가서 값을 보내줘야함
```typeScript
import { ReactNode } from "react"

export default function SearchableLayout({

	children,

}:{

	children: ReactNode;

}) {

	return (
	
		<div>
		
			<div>임시비서치바</div>
			
			{children}
		
		</div>

	)

}
```
해당 화면을 가져올 때 

```typeScript
import SearchableLayout from '@/components/searchable-layout';

import style from './index.module.css';

import { ReactNode } from 'react';

export default function Home() {
	
	return (
	
		<>
		
		</>
	
	);

}

Home.getLayout = (page: ReactNode) => {

return <SearchableLayout>{page}</SearchableLayout>

}
```
하단의 내용처럼 객체를 가져와야함 (Home 또한 객체이므로 이렇게 가져와야함.)

page 를 ReactNode 라는 타입 선언하여 SearchableLayout 화면으로 감쌈

```typeScript
import GlobalLayouts from "@/components/global-layout";

import "@/styles/globals.css";

import { NextPage } from "next";

import type { AppProps } from "next/app";

import { ReactNode } from "react";

type NextPageWithLayout = NextPage & {

	getLayout? : (page:ReactNode) => ReactNode;

};

  

export default function App({

	Component,
	
	pageProps

}: AppProps &{

	Component: NextPageWithLayout;

}) {

	const getLayout = Component.getLayout ?? ((page :ReactNode)=> page);
	
	return (
		<>
			<GlobalLayouts>
				{getLayout(<Component {...pageProps} />)}
			</GlobalLayouts>
		</>
	);
}

```
풀어서 작성하면 이렇게 됨 . 

## 사전 렌더링 , 데이터 패칭
- 리액트의 데이터 패칭
```
```