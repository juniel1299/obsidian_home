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

### Store
Redux 중앙 저장소 (이 곳에서 관리를 하게 됨 .)

