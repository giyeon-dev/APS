def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse=True)
   
    
    # 최대값 사과 상자 m개 단위로 끊기
    for i in range (len(score) // m):
        apple_box = score[m * i: m * (i + 1)]

        answer += min(apple_box) * m 
        
            
    return answer