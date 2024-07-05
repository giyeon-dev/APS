from collections import deque
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    visited = [[False] * M for _ in range(N)]
 
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            cx, cy = q.popleft()

            for dx, dy in directions:
                nx = cx + dx
                ny = cy + dy

                if 0 <= nx < N and 0 <= ny < M:
                    if matrix[nx][ny] == 1 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True

    cnt = 0
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                cnt += 1

    print(cnt)