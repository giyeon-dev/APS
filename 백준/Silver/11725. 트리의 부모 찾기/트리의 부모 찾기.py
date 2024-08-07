import sys
from collections import deque
N = int(sys.stdin.readline().strip())
G = [[0] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().strip().split())
    G[u].append(v)
    G[v].append(u)

ans = [0] * (N + 1)
q = deque()
q.append(1)

while q:
    node = q.popleft()
    for neighbor in G[node]:
        if ans[neighbor] == 0:
            ans[neighbor] = node
            q.append(neighbor)

for i in range(2, len(ans)):
    print(ans[i])