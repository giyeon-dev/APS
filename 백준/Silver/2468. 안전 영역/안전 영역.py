import sys
sys.setrecursionlimit(100000)
def safety_area(r, c, visited, rain):
    visited[r][c] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in directions:
        nr = dr + r
        nc = dc + c

        if 0 <= nr < N and 0 <= nc < N:
            if matrix[nr][nc] > rain and not visited[nr][nc]:
                safety_area(nr, nc, visited, rain)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
rain = max(max(row) for row in matrix)
def cnt_area(matrix, rain):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] > rain and not visited[r][c]:
                cnt += 1
                safety_area(r, c, visited, rain)
    return cnt

ans = []
for i in range(0, rain + 1):
    ans.append(cnt_area(matrix, i))

print(max(ans))