# 에라토스테네스의 체 


소수를 대량으로 빠르고 정확하게 구하는 알고리즘이다. (11 7 같은거)
**소수는 1과 자기 자신으로 밖에 나눠지지 않는 수이다**
**(당연히 2부터 시작한다..)**


1. 소수를 판별할 범위만큼 배열을 할당한다.
2. 해당하는 값을 넣고 소수에 해당하는 숫자가 아닐 경우 지운다. 

## 구현(자바)

일반적인 소수를 찾는 방법.

```java
import java.util.*;
import java.io.*;

public class Algorithm {

    static boolean isPrime(int n){ // 시간복잡도 O(N)
        if(n<2){
            return false; // 1은 소수가 아니기에 false
        }else{
            for(int i = 2; i < n; i++){
                if(n % i == 0) return false; // 나머지연산을 했을 때 0이 나오면 소수가 아니므로 false
            }
            return true; // 위의 case
        }
    }

    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 소수인지 판별할 숫자 input
        System.out.println( (isPrime(N) == true) ? "소수입니다" : "소수가 아닙니다.");
    }
}
```

에라토스테네스의 체 알고리즘을 사용한 경우
```java
import java.io.*;

public class Algorithm {

    static boolean[] isPrime;
    
    static void isPrime_fun(int n){ 
        isPrime = new boolean[n+1]; // N번째의 수 까지 받기위해 N+1까지 동적할당
        
        for(int i = 0; i < isPrime.length; i++){
            isPrime[i] = true; // boolean배열의 default값은 false이므로 true로 바꿔주기
        }
        
        isPrime[0] = isPrime[1] = false; // 0과 1은 소수가 아니니깐 false
        
        for(int i = 2; i <= Math.sqrt(n); i++){ // 2부터 n의 제곱근까지의 모든 수를 확인
            if(isPrime[i]){ // 해당수가 소수라면, 해당수를 제외한 배수들을 모두 false 처리하기
                for(int j = i*i; j<= n; j += i){//그 이하의 수는 모두 검사했으므로 i*i부터 시작
                    isPrime[j] = false;
                }
            }
        }
    } // isPrime_fun 함수 종료

    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 소수인지 판별할 숫자 input
        isPrime_fun(N);
    }
}
```


## 구현(파이썬)
```python
import math

MAX = 100
prime = [True for i in range(MAX+1)]

prime[1] = False

for i in range(2, int(math.sqrt(MAX))+1):
	if prime[i] == True:
    	j = 2
        while i*j <= MAX:
        	prime[i] = False
            j += 2
    
for i in range(2, number):
    if(prime[i]): print(i)	
```

100까지의 수 중에 소수를 찾도록 작성하였다 . 

배열은 0부터 시작이므로 +1을 하여 숫자를 먼저 맞춰준다

prime\[1\] = False를 통해 우선 소수가 될 수 없는 1을 제거한다. 


for 문 내용을 보면 i는 2부터 시작하며 , 마지막 값은 MAX(100) 제곱근의 최대값 + 1 즉 11이다 .

해당 내용을 통해 소수로 걸러 낼 수 있는 숫자는 2의 배수 , 3의 배수, 5의 배수, 7의 배수이다 (0부터 이므로 10까지만 )

j=2를 통해 1과 자기자신을 곱해서 나오는 수를 자동적으로 걸러내며, for문을 통해 i는 1씩 증가한다.  

그리고 i와 j 곱이 MAX (100) 를 넘어가게 된다면 , 해당 for문은 종료가 되며 체에 걸러진 소수 자리에는 True 값을 가지며, 걸러지지 않은 소수가 아닌 수들은 False 값을 가져
해당 내용을 출력하는 것으로 종료된다. 