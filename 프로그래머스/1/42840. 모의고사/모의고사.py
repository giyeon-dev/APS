def solution(answers):
    ans = []
    
    # 수포자 패턴
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    # 수포자 점수
    scores = [0, 0, 0]
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    max_score = max(scores)
    
    # 최고점 수포자 찾기
    
    for i, score in enumerate(scores):
        if score == max_score:
            ans.append(i + 1)
    return ans