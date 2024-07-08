vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    if s == 'end':
        break

    ans = f'<{s}> is acceptable.'
    cnt = 0
    for letter in s:
        if letter in vowel:
            cnt += 1

    if cnt == 0:
        ans = f'<{s}> is not acceptable.'

    vowel_cnt = 0
    consonant_cnt = 0
    for i in range(len(s) -1):
        prev_letter = s[i]

        if s[i + 1] == prev_letter:
            if prev_letter != 'e' and prev_letter != 'o':
                ans = f'<{s}> is not acceptable.'

        if prev_letter in vowel:
            if s[i+1] in vowel:
                vowel_cnt += 1
            else:
                vowel_cnt = 0

            if vowel_cnt >= 2:
                ans = f'<{s}> is not acceptable.'

        else:
            if s[i + 1] not in vowel:
                consonant_cnt += 1
            else:
                consonant_cnt = 0

            if consonant_cnt >= 2:
                ans = f'<{s}> is not acceptable.'

    print(ans)