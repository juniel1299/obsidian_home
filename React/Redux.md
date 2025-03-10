---
aliases:
  - "\bRedux"
---
# Redux
1. React , Vue , Angular 등 다양한 프론트엔드에 적용 가능한 전역 상태 관리 라이브러리
2. 컴포너트 간 상태를 공유 , 예능 가능한 상태 관리를 할 수 있음 . 

```typeScript
function App() {
  const [user, setUser] = useState(null);
  
  return (
    <div>
      <Header user={user} />
      <Main user={user} />
      <Sidebar user={user} />
    </div>
  );
}
```

이렇게 일일히 props 를 던져주지 않아도 됨 ..


## 구성 요소 
3가지의 핵심 개념으로 구성 

### Store (저장소)
Redux 중앙 저장소 (이 곳에서 관리를 하게 됨 .)

### Action (동작)
 동작에 대한 상태 변경에 필요한 명령 

### Reducer (변경 함수)
Action 이후 새로운 상태를 반환할 때 사용 
(불변성을 유지 + 새로운 상태를 반환)


## 동작 설명 
1. 컴포넌트에서 dispatch (Action)
2. Reducer가 action을 받아 상태 변경 
3. 변경된 상태가 Store 저장 -> UI 업데이트

### 예시

```typeScript
import { createSlice, configureStore } from "@reduxjs/toolkit";

// 1️⃣ 초기 상태
const initialState = { count: 0 };

// 2️⃣ Reducer (상태 변경 함수)
const counterSlice = createSlice({
  name: "counter",
  initialState,
  reducers: {
    increment: (state) => {
      state.count += 1;
    },
    decrement: (state) => {
      state.count -= 1;
    },
  },
});

// 3️⃣ Redux Store 생성
const store = configureStore({
  reducer: { counter: counterSlice.reducer },
});

// 4️⃣ 액션 내보내기
export const { increment, decrement } = counterSlice.actions;
export default store;
```

## 설치 

```npm
npm install @reduxjs/toolkit react-redux 
```

Store.ts 에서 Store 생성 (Store.ts 를 통해서 데이터 저장이 발생하도록 함 . )
```typeScript
import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./counterSlice"; // 🔥 리듀서 추가

export const store = configureStore({
  reducer: {
    counter: counterReducer, // ✅ 여러 개의 slice 추가 가능
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

Slice.ts 에서 상태 변경에 대한 상태 관리를 진행함 

```typeScript
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

interface CounterState {
  count: number;
}

const initialState: CounterState = {
  count: 0,
};

const counterSlice = createSlice({
  name: "counter",
  initialState,
  reducers: {
    increment: (state) => {
      state.count += 1;
    },
    decrement: (state) => {
      state.count -= 1;
    },
    setCount: (state, action: PayloadAction<number>) => {
      state.count = action.payload;
    },
  },
});

export const { increment, decrement, setCount } = counterSlice.actions;
export default counterSlice.reducer;
```

Provider를 통해 Redux 연결 
```typeScript
import { Provider } from "react-redux";
import { store } from "./redux/store";
import Counter from "./Counter";

function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}

export default App;
```

