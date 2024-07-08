import sys
from collections import deque
M, N = map(int, sys.stdin.readline().strip().split())
box = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 1 익은 토마토, 0 익지 않은 토마토, -1 토마토 없음
q = deque()
all_ripe = True

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            q.append((r, c))
        elif box[r][c] == 0:
            all_ripe = False

if all_ripe:
    ans = 0

directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs():
    days = -1
    while q:
        days += 1
        for _ in range(len(q)):
            cr, cc = q.popleft()
            for dr, dc in directions:
                nr = cr + dr
                nc = cc + dc

                if 0 <= nr < N and 0 <= nc < M:
                    if box[nr][nc] == 0:
                        q.append((nr, nc))
                        box[nr][nc] = 1

    return days

ans = bfs()
for r in range(N):
    for c in range(M):
        if box[r][c] == 0:
            ans = -1


print(ans)
