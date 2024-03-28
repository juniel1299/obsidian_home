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