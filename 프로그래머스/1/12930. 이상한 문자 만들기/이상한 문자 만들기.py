def solution(s):
    
    ans = []
    s = s.split(" ")
    for word in s:
        new_word = ''
        for i, char in enumerate(word):   # enumerate = idx, lst[idx]
            if i % 2 == 0:
                new_word += char.upper()
            else:
                 new_word += char.lower()
                    
        ans.append(new_word)
    return(" ".join(ans))