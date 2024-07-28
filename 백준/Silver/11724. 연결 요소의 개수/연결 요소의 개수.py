import sys
sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N + 1)] # 인접 리스트
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)