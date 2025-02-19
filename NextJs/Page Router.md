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

ex) 현재 화면에 a , b , c 라는 링크를 탈 수 있음  -> a , b , c 에 대한 페이지 ㅁ