from collections import deque
N, M = map(int, input().split())

campus = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    cnt = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        cr, cc = q.popleft()

        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if campus[nr][nc] == 'O' or campus[nr][nc] == 'P':
                    q.append((nr, nc))
                    visited[nr][nc] = True

                    if campus[nr][nc] == 'P':
                        cnt += 1

    return cnt

ans = 0
for r in range(N):
    for c in range(M):
        if campus[r][c] == 'I' and not visited[r][c]:
            ans = bfs(r, c)

if ans > 0:
    print(ans)
else:
    print('TT')