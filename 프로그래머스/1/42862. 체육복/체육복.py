def solution(n, lost, reserve):
    ans = 0
    students = [1] * (n + 1)
    
    # 잃어버린 경우
    for l in lost:
        students[l] -= 1
    
    # 여분이 있는 경우
    for r in reserve:
        students[r] += 1
    
    for i in range(1, n + 1):
        if students[i] == 1:
            continue
            
        if students[i] == 0:
            if i > 1 and students[i-1] == 2:
                students[i-1] -= 1
                students[i] += 1
            
            elif i < n and students[i+1] == 2:
                students[i+1] -= 1
                students[i] +=1
        
       
    
    for i in range(1, n+1):
        if students[i] >= 1:
            ans += 1
    
    return ans