N = int(input())

cnt = N
for _ in range(N):
    word = input()

    # 문자가 뒤에 한번이라도 나오는지 체크
    # 연속되지 않은경우 cnt -1
    for i in range(len(word)):
        if word[i] in word[i+1:]:
            if word[i] == word[i+1]:
                pass
            else:
                cnt -= 1
                break
print(cnt)