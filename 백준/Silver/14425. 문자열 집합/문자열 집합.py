import sys

N, M = map(int, sys.stdin.readline().strip().split())
S = set()

for _ in range(N):
    S.add(sys.stdin.readline().strip())

cnt = 0
for _ in range(M):
    check = sys.stdin.readline().strip()

    if check in S:
        cnt += 1

print(cnt)