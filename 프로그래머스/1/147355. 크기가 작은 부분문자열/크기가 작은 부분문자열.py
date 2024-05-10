def solution(t, p):
    
    lst = []
    for i in range(len(t)-len(p) + 1):
        lst.append(t[i: i + len(p)])
    
    cnt = 0
    for i in range(len(lst)):
        if p >= lst[i]:
            cnt += 1
        
    
    return cnt
            