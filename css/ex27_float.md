# float
- 기존 출력 정책을 따르지 않고, 자신의 위치에서 벗어나 현재 라인의 좌측(또는 우측) 끝으로 이동
**기존 영역에 남아 있지 않음**

- 또한 clear: left를 통해 뒤 따라오는 요소들을 클리어를 통해 float 제거 할 수 있음. 

```css
div{
float:left;
float:right;
clear:left;

}
```