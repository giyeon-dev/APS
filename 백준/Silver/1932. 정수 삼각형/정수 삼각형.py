n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 삼각형의 왼쪽
            dp[i][j] += dp[i-1][j]

        elif j == i: # 삼각형의 오른쪽
            dp[i][j] += dp[i-1][j-1]

        else: # 삼각형 중간
            dp[i][j] += max(dp[i-1][j-1] , dp[i-1][j])

print(max(dp[-1]))