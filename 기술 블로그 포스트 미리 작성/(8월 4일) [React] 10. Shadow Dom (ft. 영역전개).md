## “접근 금지” – Shadow DOM, 주술회전 ‘영역 전개'**
![[18eb376b4d8306bfa.jpg]]

웹 개발을 하다 보면 이런 생각이 들 때가 있다.

  

> “왜 내가 꾸민 스타일이 자꾸 깨지지…? 내 버튼은 분명히 예뻤는데…?”

(정확하겐 React 보단 Componant 영역의 내용이지만 따로 섹션이 없어서 리액트에 올리며)

내가 원치 않는 디자인이 !important 로 누군가가 올렸을 경우를 방지하기 위해 Shadow DOM 을 사용해 내가 선택한 디자인 내용들만 적중시키고 다른 디자인은 적용을 시키지 않게 할 수 있다 

### Shadow DOM이 뭐야?
  

Shadow DOM은 말 그대로 DOM의 그림자.

브라우저가 제공하는 **웹 컴포넌트(Web Components)**의 기능 중 하나로,

**외부 스타일이나 스크립트의 간섭 없이 독립적인 DOM 트리를 만들 수 있는 기능**이야.

  

예를 들어 버튼 하나를 만들었다고 해보자.
```html
<button class="a">버튼</button>
```

근데 갑자기 다른 CSS에서 .pretty 클래스를 오버라이딩해버리면?

당신의 예쁜 버튼은 **누군가의 !important 한 방**에 무너질 수도 있다.

  

주술회전의 ‘영역 전개(領域展開)’처럼

외부의 CSS가 내부로 침범하지 못하고, 내부에서 정의한 스타일만 적용되는 **비밀 공간**이 생긴다.
(단, 주술회전에서 강력한 공격을 받으면 부서지는 것 처럼 자바스크립트 로직은 통과가 된다)

###  **React에서도 Shadow DOM을 쓰나?**

여기서 헷갈리기 쉬운 포인트 하나!


> “React는 Shadow DOM을 쓴다면서요?”


실은 **React는 Shadow DOM을 쓰지 않아.**

우리가 흔히 말하는 React의 ’가상 DOM(Virtual DOM)’과 Shadow DOM은 완전히 **다른 개념**이야.
|**개념**|**설명**|
|---|---|
|Shadow DOM|브라우저가 제공하는 실제 DOM의 캡슐화 기능. 외부 CSS 간섭 차단|
|Virtual DOM|React가 DOM 조작 성능을 높이기 위해 사용하는 JS 객체. 변경 감지용|

그러니까 “React는 Shadow DOM 기반이다”라는 말은 틀린 말!

React는 Shadow DOM을 **직접 사용하지 않지만**, **커스텀 엘리먼트와 함께 쓸 수는 있어.**

### **그럼 React에서 Shadow DOM을 쓰려면?**

  

우리는 React에서도 attachShadow() API를 직접 써서 Shadow DOM을 붙일 수 있어.

하지만 좀 귀찮고 복잡하지.

  

그래서 보통은 외부 라이브러리를 써!

  
```jsx
import ShadowDOM from 'react-shadow';

function MyComponent() {
  return (
    <ShadowDOM.div>
      <style>{`p { color: red; }`}</style>
      <p>이건 Shadow DOM 안에 있어요!</p>
    </ShadowDOM.div>
  );
}
```

이렇게 감싸주면 **p 태그는 외부 CSS 영향을 받지 않고**, 이 안에서 정의한 스타일만 적용돼.

### 실무 ? 
사실 실무에서 개발자가 Shadow DOM 을 만날 일이 크진 않지만 굳이 따지면 **메인보드** 같이 단독적인 디자인이 필요한 경우나 **외부 라이브러리 컴포넌트**를 사용하게 되면 만날일이 생긴다

- 메인보드 같은 단독적인 디자인 : 외부 영향 안 받기 위해 
- 라이브러리 컴포넌트 : 본인의 라이브러리 컴포넌트 디자인을 유지하기 위해 

### **정리해보자 – Shadow DOM 핵심 요약**

- **Shadow DOM은 브라우저가 제공하는 DOM 캡슐화 기능**이다.
    
- **React는 Shadow DOM을 기본적으로 사용하지 않는다.** (가상 DOM은 다른 개념!)
    
- **원한다면 외부 라이브러리(react-shadow 등)를 이용해 사용할 수 있다.**
    
- **스타일 충돌을 방지하고 독립적인 UI 컴포넌트를 만들고 싶을 때 유용하다.**