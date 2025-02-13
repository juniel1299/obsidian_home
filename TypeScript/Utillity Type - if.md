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

```typeScript
type Exclude<T,U> = T extends U ? never : T; 

// 1. <string , boolean> <boolean , boolean> 
// 2. string | never 됨 . 
```