N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N

result = []
def backtrack(curr):
    if len(curr) == M:
        result.append(curr[:])
        return

    prev = -1
    for i in range(len(nums)):
        if not visited[i] and prev != nums[i]:
            curr.append(nums[i])
            visited[i] = True
            backtrack(curr)
            visited[i] = False
            curr.pop()
            prev = nums[i]

backtrack([])

for r in result:
    print(*r)