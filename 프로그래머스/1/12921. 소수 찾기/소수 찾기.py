import math
# 소수 찾기
def prime_num(n):
    
    if n <= 1:              # 1이하인 수의 경우 거짓
        return False 
    sqrt_n = int(math.sqrt(n))
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:      # 약수가 있는 경우 거짓
            return False

    return True
           


def solution(n):
    cnt = 0
    
    for i in range(1, n + 1):
        if prime_num(i):
            cnt += 1
        
        else:
            cnt += 0
            
    return cnt