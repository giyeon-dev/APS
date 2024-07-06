s = input()
def study_words(s):
    word = s.upper()

    word_dict = {}
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1

    mx_lst = []
    for letter, cnt in word_dict.items():
        if max(word_dict.values()) == cnt:
            mx_lst.append(letter)

    if len(mx_lst) > 1:
        ans = '?'
    else:
        ans = mx_lst[0]

    return ans

print(study_words(s))