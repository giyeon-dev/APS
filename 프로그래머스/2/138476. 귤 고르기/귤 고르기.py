def solution(k, tangerine):
    cnt = 0
    
    count_dict = {}
    
    for t in tangerine:
        if t in count_dict:
            count_dict[t] += 1
        else:
            count_dict[t] = 1
    
    lst = sorted(count_dict.values(), reverse = True)
    
    while k > 0:
        for n in lst:
            k -= n
            cnt += 1
            
            if k <= 0:
                break

    return cnt