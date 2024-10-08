
dp = [0] * 1001 # 재귀적 팰린드롬 파티션 개수 리스트
dp[1] = 1

'''
홀수: i-1의 모든 파티션에 중앙에 1을 추가하면 i의 파티션
짝수: i-1의 파티션에 1을 추가하는 경우 + i/2의 파티션을 두 번 반복하는 경우
'''
for i in range(2, 1001):
    if i % 2 == 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i // 2]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])

