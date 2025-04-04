N, K = map(int, input().split())
nums = list(map(int, input().split()))

temp_sum = sum(nums[:K])
max_sum = temp_sum

for i in range(K, N):
    temp_sum = temp_sum - nums[i - K] + nums[i]
    max_sum = max(max_sum, temp_sum)

print(max_sum)