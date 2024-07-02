N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    n, m = map(int, input().split())
    G[n].append(m)
    G[m].append(n)

v = 1
visited = []
def dfs(v):
    visited.append(v)

    for i in G[v]:
        if i not in visited:
            dfs(i)
    return visited

ans = len(dfs(v)) -1

print(ans)