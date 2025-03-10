# Recoil

리액트 상태 관리 라이브러리. 
Redux와 동일하지만 가볍다는 장점이 존재 + Context API 보다 성능 좋고 직관적임 . 

## 설치 

npm install recoil 터미널에 작성 

## 설정 방법 
App 파일에 프로젝트를 RecoilRoot로 감싸주면 됨 . 

```typeScript
import { RecoilRoot } from "recoil";
import Counter from "./Counter";

function App() {
  return (
    <RecoilRoot>
      <h1>🚀 Recoil 상태 관리 연습</h1>
      <Counter />
    </RecoilRoot>
  );
}

export default App;
```

### 전역상태
Recoil 내부에 