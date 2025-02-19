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

파일명을 \[id].tex