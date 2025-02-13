# 유틸리티 타입
실무에서 자주 사용되는 타입들을 쓰기 편하게 만듬
## 맵드 기반
- Partial\<T\> : 모든 객체의 프로퍼티를 선택적 프로퍼티 (? 뒤에 붙음) 로 바꿈
- Readonly\<T\> : T 안의 객체 내에 존재하는 프로퍼티를 모두 readonly 적용
- Required\<T\> : T 안의 객체 내 존재하는 프로퍼티를 모두 필수 프로퍼티 적용

- Pick\<T,K\> : 객체의 프로퍼티 중 내가 원하는 것만 골라서 쓸 수 있음.
- Omit\<T,K\> : 객체의 프로퍼티 중 내가 제거 할 프로퍼티를 정함.
- Record\<K,V\> : 객체 타입을 정의 할 때 반복되는 내용을 간단하게 정의 할 수 있게 해줌. 
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
-> Partial 을 적용하면 안에 프로퍼티가 모두 ? 가 붙은 것과 같아짐 (선택적 프로퍼티) , (에러 사라짐)


```typeScript
type Partial<T> = {
	[key in keyof T]? : T[key]; // 인덱스드 엑세스 타입 (특정 개체에서 타입 추출)
}
```

이것과 같은 내용임 . 


### Required\<T\>
- Partial 과 반대로 필수 프로퍼티로 만들어버림 (선택적 프로퍼티 x) , 무조건 존재해야함

```typeScript
const withThumbnailPost : Required<Post> = {
	title : "ㅇㅇ",
	tags:['ts'],
	content:'2',
	thumbnailURL:'11',
};
```

```typeScript
type Required<T> = {

	[key in keyof T]-?: T[key];

}
```
이것과 같은거임  (-?)


### readonly 
- 모든 프로퍼티를 읽기전용 프로퍼티로 만들어버림. (수정불가)

```typeScript

const readonlyPost: Readonly<Post> = {
	title:'ㅇㅇ',
	tags:[],
	content:'ㅇㅇ',
};
```

```typeScript
type Readonly<T> = {
	readonly [key in keyof T] : T[key];
};
```
위와 같은 내용임.


### Pick\<T,K\>
- 내가 원하는 프로퍼티만 골라서 쓸 수 있음.
- \<객체,사용 할 프로퍼티\> 구조로 생김. 
```typeScript
interface Post {

	title: string;
	tags: string[];
	content: string;
	thumbnailURL?:string;

}

  

const legacyPost : Pick<Post,"title" | "content"> = {

	title:'??',
	content:'??!',

};
```
```typeScript
type Pick<T,K extends keyof T> = {

	[key in K]: T[key];

}
```
해당 내용과 같은 내용임.

### Omit\<T,K\>
- 객체 타입으로부터 특정 프로퍼티를 제거하는 타입 
- Omit\<객체,제거 할 프로퍼티\>
```typeScript
const noTitlePost : Omit<Post,'title'> = {

	content:'ㅇㅇ',
	tags:[],
	thumbnailURL:'ㅇㅇ'
}
```

```typeScript
type Omit<T,K extends keyof T> = Pick<T, Exclude<keyof T,K>>;
```

해당 내용 과 같음. 

### Record\<K,V\>

- 객체 타입을 정의 할 때 반복되는 내용을 간단하게 정의 할 수 있게 해줌. 

```typeScript
type Thumbnail = Record<"large" | "medium" | "small", { url: string}>;
```
Record\<키값,{밸류:타입}\> 이렇게 작성하며 반복되는 내용을 간단하게 타입 선언 해줌 . 

