def solution(citations):
    
    citations.sort(reverse=True)
    
    h_idx = 0
    for idx in range(len(citations)):
        if citations[idx] >= idx + 1:
            h_idx = idx + 1
        else:
            break

    return h_idx
        