paper = [[0] * 100 for _ in range(100)]
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            ans += 1

print(ans)
