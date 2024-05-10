def solution(n, m):
    
    
    # 최대 공약수
    max_divisor = 0
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            max_divisor = i
            break
            
    # 최소 공배수
    min_divisor = max(n, m)
    for j in range(max(n, m), (n*m)+1):
        if j % n == 0 and j % m == 0:
            min_divisor = j
            break
            
            
    
    return [max_divisor, min_divisor]
            