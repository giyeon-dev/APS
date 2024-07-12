import sys
N, M = map(int, sys.stdin.readline().strip().split())

dict = {}
for _ in range(N):
    site, pw = sys.stdin.readline().strip().split()
    dict[site] = pw

for _ in range(M):
    target = sys.stdin.readline().strip()
    print(dict[target])
