
## 타입 스크립트 설정

터미널에 npm init -> 모든 항목 엔터로 node 초기화 

npm i @types/node 를 통해 타입스크립트 내용 설치 

npm install typescript -g 를 통해 타입스크립트 컴파일러 설치 (컴퓨터 전체)

tsc -v 를 통해 타입스크립트 버전 확인 가능

tsc src/index.ts (경로) 하게 되면 컴파일 결과 값이 자바스크립트 파일로 나옴.
(결과 값이 나오게 되면 number 는 의미 없어져서 에러 발생함)

변환된 파일은 node 를 통해 확인 가능  
( node 파일경로 )

일일히 확인할 떈 위에 tsc 경로 를 통해 확인 할 수 있지만 

**node 20 이후로는 사용x**
일괄적으로 확인 할 땐
우선 npm install ts-node -g 를 통해 설치 후 

ts-node src/index.ts 를 하면 되는데 (node 20 버전 이상부턴 에러 남)



**node 20 이후 사용법**
일괄적으로 확인 할 땐

npm install -g tsx 

이후 확인 할 땐 tsx 경로 하면 됨 



## 컴파일러 옵션 
타입 오류를 얼마나 엄격하게 검사 할 것 인지?
자바스크립트 코드의 버전은 어떻게 할 것 인지?
프로젝트 마다 설정 가능.

tsc --init 으로 초기화  (tsconfig.json 파일 생성)

### tsconfig.json 옵션
include : 특정 폴더를 한꺼번에 컴파일 하도록 설정 가능 

{
"include": ["src"]
}
터미널에서 tsc -> 해당 폴더 내부 컴파일 해줌 

target :타입스크립트 ->  자바스크립트 전환 될 떄 자바스크립트 버전 설정 (ESNext 는 가장 최신 버전 가져옴)
module : ts 에서 js로 바꿀 때 해당하는 모듈의 문법으로 변환시킴
outDir : ts 에서 js 바꿀 때 js 파일 위치 지정
strict : 엄격한 타입 검사 모드 (js -> ts 마이그레이션 시 끔)
moduleDetecion : 전역 모듈로 검사하는 타입스크립트 특성으로 인해 오류 나는 것을 해결함 
(그냥 자동으로 export{} 를 파일 마다 붙임 )
ts-node  의 esm : esm 모듈로 돌아가게 하는 내용 (**단 , 20버전 이상부턴 안 됨 .**)
(**20 이상은 skipLibCheck를 이용**) -> 사용 시 undici-types 같은 에러가 더 이상 안 발생함.
{
	"compilerOptions": {
		"target" : "ES5",
		"module" : "CommonJS"
		"outDir": "dist",
		"strict": true,
		"moduleDetection": "force",
		"skipLibCheck": true,
	},
	"ts-node": {
		"esm": true,
	},
}


