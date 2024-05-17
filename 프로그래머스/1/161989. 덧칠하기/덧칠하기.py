def solution(n, m, section):
    cnt = 0 
    start = 0
    
    for i in range( len(section)):
        if section[i] > start:
            cnt += 1
            start = section[i] + m - 1 
              

    return cnt