def solution(prices):
    ans = []
    
    for i in range(len(prices)):
        p = prices[i]
        seconds = 0
        for j in range(i + 1, len(prices)):
            seconds += 1
            if p > prices[j]:
                break
        
        ans.append(seconds)
        
    
    return ans