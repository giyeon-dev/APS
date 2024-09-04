import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 누적 합 배열
cum_sum = [[0] * (M + 1) for _ in range(N + 1)]

# 현재 위치의 값 + 현재 행의 이전 열까지 누적합 + 현재 열의 이전 행까지 누적합 - 중복 부분
for r in range(1, N + 1):
    for c in range(1, M + 1):
        cum_sum[r][c] = matrix[r-1][c-1] + cum_sum[r][c-1] + cum_sum[r-1][c] - cum_sum[r-1][c-1]


K = int(input().strip())

# 전체 합에서 위쪽과 왼쪽 합 빼고 중복 부분 더함
for _ in range(K):
    i, j, x, y = map(int, input().split())
    ans = cum_sum[x][y] - cum_sum[i-1][y] - cum_sum[x][j-1] + cum_sum[i-1][j-1]

    print(ans)