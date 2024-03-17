# form의 자식 태그
- 입력 양식
## input 태그

- 단독 태그 
- 인라인 태그
	- input.type : 입력 컨트롤 종류  
	- input.name : 서버로 전송할 때 사용하는 식별자
	- input.id : 식별자 . CSS,JS에서 주로 사용
	- input.class : 식별자 CSS,JS에서 주로 사용
	- input.size : 컨트롤의 너비(입력받는 문자 수 )
	- input.maxlength : 최대 입력 문자 수 
	- input.value : 컨트롤의 입력값
	- input.readonly : 읽기 전용. 플래그형 + 입력(X) + 서버 전송(O)
	- input.disabled : 비활성화. 플래그형  + 입력(X) + 서버 전송(X)
	- input.accesskey : 바로가기(니모닉, Nemonic)
	- input.autofocus : 자동 포커스
	- input.title : 풍선 도움말 


## 암호 상자 , Password Box, Masked TextBox

- 모든 속성이 텍스트 박스와 동일
- value 속성 금지 
```html
<form action="">
    <input type="password">
</form >
```


## 다중 라인 텍스트 박스
- \<textarea\>\</textarea\>
- 쌍 태그
- 인라인 태그
- 대부분의 속성은 텍스트와 동일
- maxlength 속성이 없다.
- textarea는 컨트롤 이므로 코드에서 띄어쓰기, 줄 바꿈이 그대로 인식 됨 


## 체크박스
- 논리값 입력
- label 태그를 이용해 글자랑 연동 가능.  
- 단일 선택 or 다중 선택 


## 라디오 버튼
- 단일값 
- 단독으론 해제 못 함 
- name을 통해 그룹을 지어줘야 함


## 셀렉트 박스
- 콤보 박스, 드랍 다운 리스트 등등...

- select 태그와 option 태그를 섞어서 씀 


## file
- 파일 업로드
- 첨부 파일

## 히든 태그
- 안 보이는 컨트롤
- 개발자용
- 전송은 해야되는데, 사용자에게 보이면 안되는 값들을 전송


## 버튼
- 전송 버튼
- 이미지 버튼
- 취소 버튼



여기까지 HTML 4.01 + XHTML 1.0






