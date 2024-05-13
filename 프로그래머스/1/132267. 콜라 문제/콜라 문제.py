def solution(a, b, n):
    ans = 0
    
    while n >= a:
        coke = (n // a) * b  # 받을 수 있는 새로운 콜라
        leftover = n % a     # 마트에 준 콜라를 제외한 나머지
        
        ans += coke
        n = coke + leftover
        
    return ans