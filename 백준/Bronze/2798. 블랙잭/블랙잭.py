N, M = map(int, input().split())
nums = list(map(int, input().split()))

def blackjack(N, M, nums):
    mx_sm = 0

    # 모든 경우 탐색, 최대한 가까운 수 업데이트
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                sm = nums[i] + nums[j] + nums[k]
                if sm <= M:
                   mx_sm = max(mx_sm, sm)
    return mx_sm

print(blackjack(N,M,nums))


