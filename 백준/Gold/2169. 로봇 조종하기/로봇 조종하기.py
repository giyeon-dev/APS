N, M= map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[-float('inf')] * M for _ in range(N)]

# 첫번째 행 초기화 (왼 -> 오 이동만 가능)
dp[0][0] = matrix[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + matrix[0][j]

for i in range(1, N):
    left_to_right = [-float('inf')] * M
    right_to_left = [-float('inf')] * M

    # 위의 행
    left_to_right[0] = dp[i-1][0] + matrix[i][0]

    # 왼 -> 오
    for j in range(1, M):
        left_to_right[j] = max(left_to_right[j-1], dp[i-1][j]) + matrix[i][j]

    # 오 -> 왼
    right_to_left[M-1] = dp[i-1][M-1] + matrix[i][M-1]
    for j in range(M-2, -1, -1):
        right_to_left[j] = max(right_to_left[j+1], dp[i-1][j]) + matrix[i][j]

    # 최대값
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])


print(dp[N - 1][M - 1])
