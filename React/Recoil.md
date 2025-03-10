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
Recoil 내부에 atom 을 이용해서 전역 상태를 선언함 . 
(Redux의 store 개념과 비슷함)  

```typeScript
import { atom } from "recoil";

// ✅ 전역 상태 (카운터 상태)
export const counterState = atom({
  key: "counterState", // 유니크한 key 값
  default: 0, // 초기값
});
```

### 상태 읽기 + 수정
useState의 개념과 매우 비슷..  

Recoil에선 useRecoilState 를 사용함.. (읽기 + 수정)

```typeScript
import { useRecoilState } from "recoil";
import { counterState } from "../recoil/counterState";

const Counter = () => {
  const [count, setCount] = useRecoilState(counterState); // Recoil 전역 상태

  return (
    <div>
      <h2>📌 현재 카운트: {count}</h2>
      <button onClick={() => setCount(count + 1)}>➕ 증가</button>
      <button onClick={() => setCount(count - 1)}>➖ 감소</button>
    </div>
  );
};

export default Counter;
```

읽기만 할 경우 useRecoilValue , 수정만 할 땐 useSetRecoilState 사용 . 




