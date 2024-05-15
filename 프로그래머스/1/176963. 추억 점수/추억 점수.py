def solution(name, yearning, photo):
    ans = []
    
    dict = {name[i]:yearning[i] for i in range(len(name))}
    
    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dict.keys():
                sum += dict[photo[i][j]]
                
        ans.append(sum)
    
    return ans