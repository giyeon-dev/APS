import sys
N, M = map(int, sys.stdin.readline().strip().split())
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 누적합 배열
sm = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sm[i][j] = sm[i-1][j] + sm[i][j-1] - sm[i-1][j-1] + matrix[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    ans = sm[x2][y2] - sm[x1-1][y2] - sm[x2][y1-1] + sm[x1-1][y1-1]
    print(ans)

