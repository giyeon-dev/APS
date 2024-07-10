from collections import deque
def bfs(N, cr, cc, tr, tc):
    q = deque()
    q.append((cr, cc, 0))
    visited = [[False] * N for _ in range(N)]
    visited[cr][cc] = True

    directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    while q:
        cr, cc, dist = q.popleft()

        if cr == tr and cc == tc:
            return dist

        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    q.append((nr, nc, dist + 1))
                    visited[nr][nc] = True

T = int(input())
for _ in range(T):
    N = int(input())
    cr, cc = map(int, input().split())
    tr, tc = map(int, input().split())

    ans = bfs(N, cr,cc,tr, tc)
    print(ans)