터미널에 npm init -> 모든 항목 엔터로 node 초기화 

npm i @types/node 를 통해 타입스크립트 내용 설치 

npm install typescript -g 를 통해 타입스크립트 컴파일러 설치 (컴퓨터 전체)

tsc -v 를 통해 타입스크립트 버전 확인 가능

tsc src/index.ts (경로) 하게 되면 컴파일 결과 값이 자바스크립트 파일로 나옴.
(결과 값이 나오게 되면 number 는 의미 없어져서 에러 발생함)

변환된 파일은 node 를 통해 확인 가능  
( node 파일경로 )

일일히 확인할 떈 위에 tsc 경로 를 통해 확인 할 수 있지만 

일괄적으로 확인 할 땐
npm install ts-node -g 를 통해 설치 후 

