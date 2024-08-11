N = int(input())
M = int(input())
S = input()

target = ''
for i in range(2 * N + 1):
    if i % 2 == 0:
        target += 'I'
    else:
        target += 'O'

cnt = 0
for i in range(M - len(target) + 1):
    letter = ''
    for j in range(i, i + len(target)):
        letter += S[j]

    if letter == target:
        cnt += 1

print(cnt)