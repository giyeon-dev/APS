def solution(left, right):
    answer = 0
    
    # 약수의 개수
    for n in range(left, right+1):
        cnt = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
    
    # 홀수 짝수 판별
        if cnt % 2 == 0:
            answer += n
        else:
            answer -= n
            
    return answer