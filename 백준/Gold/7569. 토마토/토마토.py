from collections import deque
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


def bfs():
    q = deque()

    # 익어 있는 토마토 큐에 삽입
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 1:
                    q.append((h, n, m))

    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while q:
        h, n, m = q.popleft()

        for dh, dn, dm in directions:
            nh, nn, nm = h + dh, n + dn, m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and tomato[nh][nn][nm] == 0:
                tomato[nh][nn][nm] = tomato[h][n][m] + 1
                q.append((nh, nn, nm))


bfs()
ans = 0
all_ripe = True
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:
                all_ripe = False
            ans = max(ans, tomato[h][n][m])

if all_ripe:
    print(ans - 1)
else:
    print(-1)
