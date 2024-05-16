# 약수 개수 구하기: 제곱근 활용
import math

def cnt_divisors(n):
    cnt = 0
    sqrt_n = int(math.sqrt(n))  
    for i in range(1, sqrt_n + 1): 
        if n % i == 0:
            if i == n // i:
                cnt += 1  # 약수가 같은 경우
            else:
                cnt += 2  
    return cnt



def solution(number, limit, power):
    ans = 0
    divisor_lst = []
    
    for i in range(1, number + 1):
        divisor_lst.append(cnt_divisors(i))
    
    divisor_lst = sorted(divisor_lst)
    cnt = 0
    for i in range(len(divisor_lst)):
        if divisor_lst[i] <= limit:
            ans += divisor_lst[i]
            cnt += 1
        else:
            ans += (len(divisor_lst) - cnt) * power
            break
            
    
    return ans