def solution(n, words):

    idx = 0
    turn = 0

    used_words = set()
    for i in range(len(words)):
        
        if i > 0:
            if words[i - 1][-1] != words[i][0]:
                idx = (i % n) + 1
                turn = (i // n) + 1
                return [idx, turn]

        
        if words[i] in used_words:
            idx = (i % n) + 1
            turn = (i // n) + 1
            return [idx, turn]
        
        used_words.add(words[i])
            
    return [idx, turn]