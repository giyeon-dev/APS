def solution(phone_number):
    answer = []
    num = phone_number[-4:]
    answer.append('*'*(len(phone_number)-4))
    answer.append(num)
    return ''.join(answer)