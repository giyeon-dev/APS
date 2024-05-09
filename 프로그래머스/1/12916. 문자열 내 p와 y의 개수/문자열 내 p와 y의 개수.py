def solution(s):
    answer = True
    p_cnt = y_cnt = 0
    # 소문자로 변경
    s = s.lower() 

    # 문자열 탐색
    for i in s:
        if i == 'p':
            p_cnt += 1
        elif i == 'y':
            y_cnt += 1
    
    # 개수 비교
    if p_cnt != y_cnt:
        answer = False

    return answer