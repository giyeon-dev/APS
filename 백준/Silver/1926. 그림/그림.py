from collections import deque
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
def bfs(r, c, visited):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    size = 0
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    while q:
        cr, cc = q.popleft()
        size += 1

        for dr, dc in directions:
            nr = cr + dr
            nc = cc + dc

            if 0 <= nr < n and 0 <= nc < m:
                if paper[nr][nc] == 1 and not visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = True

    return size

paint = 0
size_lst = []
for r in range(n):
    for c in range(m):
        if paper[r][c] == 1 and not visited[r][c]:
            ans = bfs(r, c, visited)
            size_lst.append(ans)
            paint += 1

        if paint == 0:
            size_lst.append(0)

print(paint)
print(max(size_lst))
