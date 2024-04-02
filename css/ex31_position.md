# position (요소의 위치)
1. padding > 부모가 자식의 위치 지정
2. margin > 스스로 위치가 바뀜
3. position > FM(CSS1, CSS2, CSS3)
4. transform > FM(CSS3)


## position
- 좌표값 사용 > 위치 사용
- x(left) , y(top)
- 좌표를 지정하는 방식이 여러개 제공 > 기준점이 다르다..

1. position : static;
	- 기본 값

2. position : absolute;
	- 절대 좌표
	- left, top > 좌표 지정
	- 문서의 좌측 상단을 원점으로 한다 (X) > 자신의 직계 조상 중 가장 처음으로 만나는 태그를 기준으로 한다.
	- 원래 있는 공간은 사라진다.

3. position : relative;
	- 상대 좌표
	- left, top > 좌표 지정
	- 자신의 원래 위치를 원점으로 한다.
	- 원래 있는 공간은 그대로 유지된다. (기준점 역할)


4. position: fixed;
	- 고정 좌표
	- left top > 좌표 지정
	- 문서 좌측 상단이 원점이 아님 > 브라우저 창 좌측 상단을 원점으로 함 
	- 원래 있는 공간은 사라진다.


