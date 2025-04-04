N, K = map(int, input().split())
nums = list(map(int, input().split()))

temp_sum = sum(nums[:K])
max_sum = temp_sum

for i in range(N-K):
    temp_sum += nums[K + i] - nums[i]
    max_sum = max(max_sum, temp_sum)

print(max_sum)