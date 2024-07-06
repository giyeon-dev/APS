from collections import deque
N, M = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

matrix = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs(r, c):
    q = deque() # queue 초기화
    q.append((r, c)) # 시작점 삽입
    visited[r][c] = True # 방문 체크

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        sr, sc = q.popleft()

        for dr, dc in directions: # 가로 세로 방향 이동
            nr = sr + dr
            nc = sc + dc

            if 0 <= nr < N and 0 <= nc < M: # 범위 체크
                if land[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    matrix[nr][nc] = matrix[sr][sc] + 1



for r in range(N):
    for c in range(M):
        if land[r][c] == 2 and not visited[r][c]:
            bfs(r, c)

for r in range(N):
    for c in range(M):
        if land[r][c] == 1 and matrix[r][c] == 0:
            matrix[r][c] = -1

for i in range(N):
    print(*matrix[i])