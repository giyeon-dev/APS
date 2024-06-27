N = int(input())
nums = list(map(int, input().split()))
def avgscore(N, nums):
    M = max(nums)
    new_scores = [(n / M) * 100 for n in nums]
    ans = sum(new_scores) / N
    return ans


print(avgscore(N, nums))
