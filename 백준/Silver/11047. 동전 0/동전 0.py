import sys
N, K = map(int, sys.stdin.readline().strip().split())
lst = []
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    lst.append(n)

lst.sort(reverse=True)

cnt = 0
for coin in lst:
    if K >= coin:
        cnt += K // coin
        K %= coin

print(cnt)