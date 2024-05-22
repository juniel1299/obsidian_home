# REST API , RESTful Service
- REST, Representational State Transfer
- 웹상의 자원(문서,이미지,동영상,데이터 등)을 자원명으로 표시해서 자원의 상태를 주고 받기 행위
- HTTP URI를 통해서 자원을 명시하고, HTTP Method를 통해서 자원에 대한 CRUD 처리하는 방식
- 기존에 생성하는 URL의 형식(X) > 별도의 규칙을 만족하는 URL을 생성 O 

## URI 작성
1. 기존 방식
- GET \http://localhost/member/list.do 목록보기
- POST \http://localhost/member/add.do 추가하기
- POST \http://localhost/member/edit.do 수정하기