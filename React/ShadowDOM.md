# Shadow DOM (쉐도우 돔)  

1. 캡슐화  : HTML , CSS , JS 기존 코드들과 분리가 가능 (새로 입혀줘야함)  
2. 재사용성 : 하나의 컴포넌트가 여러 곳에서 충돌 x  


## 생성 
react-shadow 에서 import 후 사용 가능  

const shadowHost = document.querySelector('#my-element');  -> 쉐도우 돔으로 지정 할 id  
const shadowRoot = shadowHost.attachShadow({ mode: 'open' });  -> (mode 가 open 이면 외부에서 접근 가능 , close 면 외부에서 접근 불가능 )  

## 예시 
```javaScript
class MyComponent extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML = `
      <style>
        p { color: green; }
      </style>
      <p>Shadow DOM inside custom element</p>
    `;
  }
}

customElements.define('my-component', MyComponent);

<my-component></my-component>
```

### 구조

/components/  
├── ppp.js           ← Shadow DOM 포함한 컴포넌트 정의  (화면 + 동작)  
├── pppLogic.js      ← Shadow DOM 내부 동작 로직  (쉐도우 돔 내부에서 쓸 동작)  
├── pppTemplate.html ← (선택) HTML 템플릿  
├── pppStyle.css     ← (선택) 스타일  

### 예시 
React 에서   
ppp.js 을 동작 + 화면 작성  
pppLogic.js 를 Shadow DOM 에서 쓸 동작 작성  

Next 에서  
ppp.js 파일 -> page.js 과 역할 동일  (페이지 파일)  
pppLogic.js -> usePPPLogic 과 역할 동일 (동작 파일)    


**이라는 모듈화, 분리, 역할 나누기 개념은 동일 ( 완전 일치 x )**  


단 
Shadow DOM 쪽은 브라우저 레벨의 DOM 캡슐화  

Next.js는 프레임워크 레벨의 파일/기능 분리  
