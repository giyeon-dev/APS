def solution(k, score):
    ans = []
    
    prize = []
    
    for idx, n in enumerate(score):
        if idx <= (k - 1):
            prize.append(n)
        
        elif idx > (k - 1) and score[idx] > min(prize):
            prize.remove(min(prize))
            prize.append(n)
    
        ans.append(min(prize))
            
    return ans