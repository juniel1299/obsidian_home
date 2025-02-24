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
```typeScript
const fetchData = async () => {
	const response = await fetch('...');
	const data = await response.json();
	setState(data);
};

useEffect(()=> {
	fetchData();
},[]);
return (
	<div>데이터 리턴</div>
)
```

1. 불러온 데이터를 저장 할 State 생성 
2. 데이터 패칭 함수 
3. 컴포넌트 마운트 시점에 fetchData 호출 (useEffect)
4. (데이터 로딩중일때 예외처리)

단점 : 초기 접속 요청부터 데이터 로딩까지의 시간이 오래 걸림
(FCP 도 기다려야하는데 API도 기다려야 하기 떄문 ...)
(앞에서 말했듯이 Next는 사전 렌더링으로 통해 FCP 가 빠름)

- Next 데이터 패칭 
1. 사전 렌더링 중 발생함 (마운트 이후에도 발생 가능함.)
-> 데이터 요청 시점이 매우 빨라짐 


### 사전 렌더링 SSR
- 가장 기본적인 사전 렌더링 방식
- 욫어이 들어올 때 마다 사전 렌더링을 진행
```typeScript

//컴포넌트보다 먼저 실행되어서, 컴포넌트에 필요한 데이터를 불러오는 함수
export const getServerSideProps = () => {

//컴포넌트보다 먼저 실행되어서, 컴포넌트에 필요한 데이터를 불러오는

	const data = 'hello';
	
	return{
	
		props: {
		
			data,
		
		},
	
	};

};

export default function Home(
	{data}:InferGetServerSidePropsType<typeof getServerSideProps>
) {

	return (
	
		<div className={style.container}>
	
		<section>
	
			<h3>
	
				지금 추천하는 도서
	
				{books.map((book)=> <BookItem key={book.id} {...book}/>)}
	
			</h3>
	
		</section>
	
		<section>
		
			<h3>
			
				등록된 모든 도서
				
				{books.map((book)=> <BookItem key={book.id} {...book}/>)}
				
			</h3>
		
		</section>
	
	</div>
	
	);

}
```

해당 코드를 작성하게 되면 SSR 방식으로 사전 렌더링 해옴

해당 코드가 컴포넌트보다 먼저 동작함 (백엔드 데이터 끌어올 때 유용)

서버 측에서만 1번 동작 하는 것 이기 떄문에 console.log 같은건 안 됨 (대신 터미널에 나옴)
(퍼블리싱js 같은 window 그런건 못 씀)
### 정적 사이트 생성 SSG
사전 렌더링 중 데이터 패칭이 발생 
빌드 타임에 미리 페이지를 사전 렌더링 해 둠
빌드 타임은 유연하게 발생됨
빌드타임의 경우 JS 렌더링 (REQ , RES) 합친 내용 
빌드타임으로 인해 SSR의 단점을 보완함. 

장점 : 사전 렌더링에 많은 시간이 소요되는 페이지도 사용자의 요청에는 매우 빠르게 응답 가능 
단점 : 매번 똑같은 페이지만 응답함 , 최신 데이터 반영이 어려움 (정적 데이터 화면에서 강함)

```typeScript
import SearchableLayout from '@/components/searchable-layout';

import style from './index.module.css';

import { ReactNode, useEffect } from 'react';

import BookItem from '@/components/book-item';

import { InferGetServerSidePropsType } from 'next';

import fetchBooks from '@/lib/fetch-books';

import fetchRandomBooks from '@/lib/fetch-random-books';

  

export const getStaticProps = async () => {

  

//컴포넌트보다 먼저 실행되어서, 컴포넌트에 필요한 데이터를 불러오는

const [allBooks, recoBooks] = await Promise.all([

	fetchBooks(),
	
	fetchRandomBooks(),

])

	return {
	
		props: {
		
			allBooks,
			
			recoBooks,
		
		},
	
	};

};

export default function Home({allBooks,recoBooks}:InferGetServerSidePropsType<typeof getStaticProps>) {

  

	return (
	
		<div className={style.container}>
		
				<section>
				
					<h3>
					
						지금 추천하는 도서
						
						{recoBooks.map((book)=> <BookItem key={book.id} {...book}/>)}
					
					</h3>
				
				</section>
			
			<section>
		
				<h3>
	
					등록된 모든 도서
					
					{allBooks.map((book)=> <BookItem key={book.id} {...book}/>)}
			
				</h3>
	
			</section>
	
		</div>
	
		);

}

  

Home.getLayout = (page: ReactNode) => {

	return <SearchableLayout>{page}</SearchableLayout>

}
```
getStaticProps 로 바꾸면 SSG로 됨 . 
(단 개발모드(dev)에서 확인 불가 확인시 npm run build )
(SSG는 흰색 원으로 표시 , SSR은 함수 기호로 표시, 아무 설정도 없으면 빈 원으로 표시됨)

#### 정적인 경우
```typeScript
import SearchableLayout from "@/components/searchable-layout";

import { ReactNode, useEffect, useState } from "react";

import BookItem from "@/components/book-item";

import { GetServerSidePropsContext, GetStaticPathsContext, InferGetServerSidePropsType } from "next";

import fetchBooks from "@/lib/fetch-books";

import { useRouter } from "next/router";

import { BookData } from "@/type";

  

// export const getStaticProps = async (context : GetStaticPathsContext) => {

// // 쿼리 스트링으로 검색 가능 ..

// const q = context.query.q;

// const books = await fetchBooks(q as string);

// return {

// props : {

// books,

// },

// }

// }

export default function Page () {

const [books,setBooks] = useState<BookData[]>([]);

const router = useRouter();

const q = router.query.q;

  

const fetchSearchResult = async () => {

const data = await fetchBooks(q as string);

setBooks(data);

}

useEffect(()=> {

if(q){

fetchSearchResult();

}

},[q])

  

return (

<div>

{books.map((book) => (

<BookItem key={book.id} {...book}/>

))}

</div>

)

}

  
  

Page.getLayout = (page:ReactNode) => {

return (

<SearchableLayout>{page}</SearchableLayout>

)

}
```
#### 동적인 경우
getStaticPaths 를 사용해야함. 


```typeScript
import { GetServerSideProps, GetServerSidePropsContext, GetStaticPropsContext, InferGetServerSidePropsType, InferGetStaticPropsType } from "next";

import style from "./[id].module.css";

import fetchOneBook from "@/lib/fetch-one-book";

  

export const getStaticPaths = () => {

	return {
	
		//어떤 경로가 있을 수 있는지 미리 알려주기 위해 배열로 전달
		
		paths: [
			{params : { id : '1'}},
			{params : { id : '2'}},
			{params : { id : '3'}},
		],
		//존재하지 않는 경우 대비 (false 시 notfound 적용됨.)
		fallback: false,
	}
}

  

export const getStaticProps = async (context: GetStaticPropsContext) => {

	const id = context.params!.id;
	
	const book = await fetchOneBook(Number(id));

	return {
	
		props : {
		
			book,
		
		},
	
	};

}

export default function Page({

	book,

}: InferGetStaticPropsType<typeof getStaticProps>) {

  

	if(!book) return "에러";

  

	const { id, title, subTitle,description,author,publisher,coverImgUrl } = book;

  

	return (
	
	<div className={style.container}>
	
	<div className={style.cover_img_container} style={{backgroundImage:`url('${coverImgUrl}')`}}>
	
	<img src={coverImgUrl}/>
	
	</div>
	
	<div className={style.title}>
	
	{title}
	
	</div>
	
	<div className={style.subTitle}>
	
	{subTitle}
	
	</div>
	
	<div className={style.author}>
	
	{author} | {publisher}
	
	</div>
	
	<div className={style.description}>
	
	{description}
	
	</div>
	
	</div>
	
	)

}
```
해당 화면에서 이동 할 수 있는 경로를 미리 알려야하기 때문에 배열에 다 담아야함 . 
만약 없으면 fallback을 통해 notfound로 보낼 수 있음

없는 값은 빌드타임에 들어 갈 수 없음 
(단 , fallback:'blocking' 또는 true 로 설정하게 되면 가능함.)
(blocking의 경우 화면 Props 동시에 렌더링해서 보내줌)
(true는 Props 없이 우선 화면만 렌더링으로 먼저 보내고 Props만 따로 계산해서 렌더링)

- false : 404 
- blocking : SSR
- true : SRR + 데이터가 없는 폴백 상태의 페이지부터 변환
### 증분 정적 재생성(ISR)

- SSG 방식으로 생성된 정적 페이지를 일정 시간을 주기로 다시 생성하는 기술 .
SSG 를 통해 접속 요청시 V1 버전의 페이지 반환이 됨
-> 내가 설정한 시간이 되면 V2 버전의 페이지 반환하고 이후에는 SSG로 V2 버전 페이지를 반환함. 
**매우 빠른 속도로 응답이 가능하고 최신 데이터 반영이 가능하다는 SSG 와 SSR 장점을 가져옴**

```typeScript
export const getStaticProps = async () => {

//컴포넌트보다 먼저 실행되어서, 컴포넌트에 필요한 데이터를 불러오는

	const [allBooks, recoBooks] = await Promise.all([
	
		fetchBooks(),
		
		fetchRandomBooks(),
	
	])

	return {
	
		props: {
		
			allBooks,
			
			recoBooks,
		
		},
	
		revalidate : 3,
	
	};

};
```
여기서 revalidate : 3 이 SSG 새로운 페이지 생성을 3초마다 한다의 의미..