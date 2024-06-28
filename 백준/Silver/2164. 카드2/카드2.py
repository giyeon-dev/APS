from collections import deque
N = int(input())

nums = deque([])
for n in range(1, N + 1):
    nums.append(n)

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums[0])