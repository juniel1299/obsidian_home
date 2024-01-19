# 메서드 오버로딩 (Method Overlo)
같은 이름의 메서드를 여러개 만드는 방법

메서드의 인자 리스트를 다양한 형태로 구성하여 같은 이름의 메서드를 여러개 만듬 

매개변수의 개수 , 매개변수의 자료형을 통해 여러개 만들 수 있음 
단, 매개변수의 이름, 반환값의 자료형을 가지고는 만들 수 없음


예시)
> 1. public static void test(){} // 가능
> 2. public static void test(){} // 불가능 (1번과 겹쳐서 안 됨)
> 3. public static void test(int n){} //가능 
> 4. public static void test(int m ){} //불가능 , 3번과 겹침
> 5. public static void test(int n, int m){} // 가능 (인자를 2개 받아야 하기 때문에 안 겹침)
> 6. public static void test(String m ){} // 불가능 (참조형 안 됨)
> 7. public static int test () {} //불가능 1번과 겹침


