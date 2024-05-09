def solution(x):
    answer = True
    
    # 각 자릿수 합 구하기
    sum = 0
    lst = list(map(int, str(x)))
    for i in range(len(lst)):
        sum += lst[i]
        
    # 하샤드 수 검사
    if x % sum != 0:
        answer = False

    return answer