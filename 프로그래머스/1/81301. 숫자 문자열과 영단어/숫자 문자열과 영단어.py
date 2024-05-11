def solution(s):
    
    num_words = {'zero': 0, 'one': 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight' : 8, 'nine' :9}
    
    ans = ''
    eng_words = ''
    for word in s:
        if '0' <= word <= '9':
            ans += word
        else:
            eng_words += word
            if eng_words in num_words.keys():
                eng_words = (num_words[eng_words])
                ans += str(eng_words)
                eng_words = ''
                   
    return int(ans)