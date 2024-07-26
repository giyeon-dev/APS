from collections import deque
M, N, K = map(int, input().split())
matrix = [[0] * (N) for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())

    for x in range(y1, y2):
        for y in range(x1, x2):
            matrix[x][y] = 1


visited = [[False] * N for _ in range(M)]

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

            if 0 <= nr < M and 0 <= nc < N:
                if matrix[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

    return size


ans_lst = []
cnt = 0
for r in range(M):
    for c in range(N):
        if matrix[r][c] == 0 and not visited[r][c]:
            ans = bfs(r, c)
            ans_lst.append(ans)
            cnt += 1


print(cnt)
print(*sorted(ans_lst))
