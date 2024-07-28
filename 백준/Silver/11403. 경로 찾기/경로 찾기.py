N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(start, visited):
    for next in range(N):
        if graph[start][next] == 1 and not visited[next]:
            visited[next] = True
            dfs(next, visited)


ans = [[0] * N for _ in range(N)]

for i in range(N):
    visited = [False] * N
    dfs(i, visited)
    for j in range(N):
        if visited[j]:
            ans[i][j] = 1


for a in ans:
    print(*a)