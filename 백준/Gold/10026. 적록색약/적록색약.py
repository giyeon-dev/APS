from collections import deque
N = int(input())
matrix = [list(input()) for _ in range(N)]


def bfs(r, c, matrix):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        cr, cc = q.popleft()
        color = matrix[cr][cc]

        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc

            if 0 <= nr < N and 0 <= nc < N:
                if color == matrix[nr][nc] and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True


visited = [[False] * N for _ in range(N)]
cnt1 = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:

            bfs(r, c, matrix)
            cnt1 += 1


visited = [[False] * N for _ in range(N)]
gb_matrix = matrix[:]
for r in range(N):
    for c in range(N):
        if gb_matrix[r][c] == 'R':
            gb_matrix[r][c] = 'G'

cnt2 = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c, gb_matrix)
            cnt2 += 1


print(cnt1, cnt2)
