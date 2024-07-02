from collections import deque
N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    n, m = map(int, input().split())
    G[n].append(m)
    G[m].append(n) # 양방향

# 그래프 인접 리스트 정렬
for v in range(1, N + 1):
    G[v].sort()
def bfs(G, V):
    visited = [V]
    queue = deque([V])

    while queue:
        cur_v = queue.popleft()
        for v in G[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

def dfs(V):
    visited.append(V)
    for v in G[V]:
        if v not in visited:
            dfs(v)
    return visited

visited = []
print(*dfs(V))
print(*bfs(G, V))