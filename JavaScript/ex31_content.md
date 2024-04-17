# BOM vs DOM 태그 조작 
1. 태그 검색 (BOM,DOM)
2. 속성 조작 (BOM,DOM)
3. *콘텐츠 조작(DOM)  BOM 못 함* 
4. 이벤트 조작 (DOM , BOM)

# Content 
- 시작 태그와 끝 태그 사이의 내용 (PCDATA , Element) 조작 
1. innerText
	- 시작 태그와 끝 태그 사이의 내용 읽기/쓰기
	- 비표준(MS)
	- 문자열 인식

2. innerHTML
	- 시작 태그와 끝 태그 사이의 내용을 읽기/쓰기 
	- 문자열 + 태그 인식

3. textContent 
	- 시작 태그와 끝 태그 사이의 내용을 읽기/쓰기
	- 표준
	- 문자열 인식

이외에도 outerText , outerHTML 존재 .



