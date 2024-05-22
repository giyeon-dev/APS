def solution(s):
    answer = ''
    words = list(s.split(' '))

    for i in range(len(words)):
        words[i] = words[i].capitalize()
      
    answer = ' '.join(words)

            
    return answer