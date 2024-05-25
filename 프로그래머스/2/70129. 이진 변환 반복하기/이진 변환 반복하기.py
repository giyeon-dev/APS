def solution(s):
    answer = []
    cnt = 0
    zero = 0
    
    while s != "1":
        temp = s.replace("0", "") # 0 제외 문자열
        zero += len(s) - len(temp)
        s = bin(len(temp))[2:]  #0b 제외
        cnt += 1
    
    answer.append(cnt)
    answer.append(zero)
    
    return answer