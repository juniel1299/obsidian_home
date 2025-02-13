# 유틸리티 타입
실무에서 자주 사용되는 타입들을 쓰기 편하게 만듬
## 맵드 기반
- Partial : 모든 객체의 프로퍼티를 선택적 프로퍼티 (? 뒤에 붙음) 로 바꿈
- Readonly\<T\> : T 안의 객체 내에 존재하는 것들을 다 readonly 적용


### Partial\<T\>
- 모든 객체의 프로퍼티를 선택적 프로퍼티로 바꾸는 유틸리티 타입
```typeScript
interface Post {

title: string;
tags: string[];
content: string;
thumbnailURL?:string;

}

  

const draft: Partial<Post> = {

title: 'ㅈㅈ',
content : 'ㅇㅇ',

}
```
Post 타입엔 4개가 존재하는데 아직 tags , thumbnailURL 에 대한 값이 없기 때문에 에러 
-> Partial 을 적용하면 안에 프로퍼티가 모두 ? 가 붙은 것과 같아짐 (선택적 프로퍼티) , (에러 )