# 조건부 타입 기반 유틸리티 
- Exclude \<T,U\>
- Extract \<T,U\>
- ReturnType\<T\>

## Exclude\<T,U\>
- T에서 U 를 제거하는 타입 

```typeScript
// string , boolean 타입에서 boolean 제거 . 
type A = Exclude <string | boolean , boolean>; 
```

