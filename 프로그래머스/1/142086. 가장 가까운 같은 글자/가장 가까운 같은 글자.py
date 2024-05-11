def solution(s):
    answer = []
    s_dict = {}
    
    for idx, char in enumerate(s):
        if char not in s_dict.keys():
            s_dict[char] = idx
            answer.append(-1)
            
        else:
            answer.append(idx - s_dict[char])
            s_dict[char] = idx 
            
    return answer