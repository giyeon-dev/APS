def solution(clothes):
    
    dict = {}
    for c in clothes:
        if c[1] in dict:
            dict[c[1]] += 1
        else:
            dict[c[1]] = 1
    
    ans = 1
    for cnt in dict.values():
        ans *= (cnt + 1)
        
    return ans - 1