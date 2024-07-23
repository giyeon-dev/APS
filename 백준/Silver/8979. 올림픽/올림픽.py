N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
gold = silver = bronze = 0
for r in arr:
    if r[0] == K:
        gold, silver, bronze = r[1], r[2], r[3]

for r in arr:
    if r[1] <= gold and r[2] <= silver and r[3] <= bronze:
        cnt += 1

ans = N - cnt

print(ans)