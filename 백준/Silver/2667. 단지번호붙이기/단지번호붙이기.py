from collections import deque
N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    size = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        cr, cc = q.popleft()
        size += 1

        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc

            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    return size


cnt = 0
ans = []
for r in range(N):
    for c in range(N):
        if matrix[r][c] == 1 and not visited[r][c]:
            result = bfs(r, c)
            ans.append(result)
            cnt += 1

ans.sort()
print(cnt)
for i in range(len(ans)):
    print(ans[i])



