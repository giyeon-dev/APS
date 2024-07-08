import sys
N, M = map(int, sys.stdin.readline().strip().split())
dict = {}
for _ in range(N):
    word = sys.stdin.readline().strip()

    if len(word) >= M:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

ans = sorted(dict.keys(), key= lambda x: (-dict[x], -len(x), x))

for a in ans:
    print(a)