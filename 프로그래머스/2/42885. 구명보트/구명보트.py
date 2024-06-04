def solution(people, limit):
    people = sorted(people)
    left = 0 # 가장 가벼운 사람 인덱스
    right = len(people) - 1 # 가장 무거운 사람 인덱스
    cnt = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1 
        else:
            right -= 1 # 아닌 경우 무거운 사람 태우기
        cnt += 1

    return cnt 