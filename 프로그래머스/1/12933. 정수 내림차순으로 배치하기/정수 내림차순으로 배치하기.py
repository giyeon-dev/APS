def solution(n):
    answer = 0
    # 아이디어: 리스트에 다 담고 큰 순으로 정렬, 그리고 합쳐서 다시 출력
    
    lst = []
    lst = list((str(n)))
    lst.sort(reverse=True)
    answer = int("".join(lst))
    
    return answer