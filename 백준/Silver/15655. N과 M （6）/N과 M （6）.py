def combinations(nums, M):
    lst = []
    def backtrack(start, curr):
        if len(curr) == M:
            lst.append(curr[:])
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

    backtrack(0, [])

    return lst


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = (combinations(nums, M))

for a in ans:
    print(*a)
