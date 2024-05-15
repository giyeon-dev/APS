def solution(s):
    ans = ''
    s = s.split(" ")
    
    # 최대값
    mx_num = -999999
    
    for i in range(len(s)):
        if mx_num < int(s[i]):
            mx_num = int(s[i])
            
    
    # 최소값
        mi_num = 999999
    
    for i in range(len(s)):
        if mi_num > int(s[i]):
            mi_num = int(s[i])
    
    ans = str(mi_num) + " " + str(mx_num)
    return ans