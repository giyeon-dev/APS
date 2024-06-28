import sys

input = sys.stdin.readline
N = int(input().strip())

# counting sort
cnt = [0] * 10001

for _ in range(N):
    n = int(input().strip())
    cnt[n] += 1

for i in range(1, 10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)

