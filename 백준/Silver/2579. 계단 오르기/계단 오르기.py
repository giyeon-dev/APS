import sys
n = int(sys.stdin.readline().strip())
scores = [0] * 301
for i in range(1, n + 1):
    scores[i] = int(sys.stdin.readline().strip())

def dp(n):
    dp = [0] * 301
    dp[1] = scores[1]
    dp[2] = scores[2] + scores[1]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])
    return dp[n]

print(dp(n))
