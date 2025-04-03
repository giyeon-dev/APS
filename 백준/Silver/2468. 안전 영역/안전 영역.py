from collections import deque

def bfs(si, sj, h):
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and area[ni][nj] > h:
                q.append((ni, nj))
                v[ni][nj] = 1


def solve(h):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and area[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    return cnt


N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]
max_h = max(max(row) for row in area)

ans = 0

for h in range(0, max_h + 1):
    v = [[0] * N for _ in range(N)]
    ans = max(ans, solve(h))


print(ans)