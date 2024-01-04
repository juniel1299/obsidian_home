# 메서드 오버로딩 Method Overloading

> 같은 이름의 메서드를 여러개 만드는 기술
> 메서드의 인자 리스트를 다양한 형태로 구성하여 같은 이름의 메서드를 여러개 만드는 기술

## 메서드 오버로딩을 하는 이유 
> 성능 개발 x , 
> 개발자에게 도움이 되기 때문에 사용

**메서드 오버로딩 구현 조건 가능한 경우**
1. 매개변수의 개수
2. 매개변수의 자료

**메서드 오버로딩 구현 조건 불가능
1. 매개변수의 이름
2. 반환값의 자료형 

## 메서드 만들 때
> 1. public static void test(){} // 가능
> 2. public static void test(){} // 불가능 (1번과 겹쳐서 안 됨)
> 3. public static void test(int n){} //가능 
> 4. public static void test(int m ){} //불가능 , 3번과 겹침
> 5. public static void test(int n, int m){} // 가능 (인자를 2개 받아야 하기 때문에 안 겹침)
> 6. public static void test(String m ){} // 불가능 (참조형 안 됨)
> 7. public static int test () {} //불가능 1번과 겹침

### 메서드 호출하기

