def solution(s):
    answer = ''
    num = len(s)
    if num % 2 != 0:
        answer = s[(num // 2)]
    else:
        answer = s[(num // 2) -1] + s[num // 2]
    return answer