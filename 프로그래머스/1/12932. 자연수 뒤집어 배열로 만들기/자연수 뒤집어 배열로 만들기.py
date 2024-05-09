def solution(n):
    answer = []
    reversed_str = str(n)[::-1]
    answer = [int(s) for s in reversed_str]
    
    return answer