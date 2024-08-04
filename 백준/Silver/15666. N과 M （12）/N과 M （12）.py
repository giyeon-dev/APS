N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))


def backtrack(start, curr):
    if len(curr) == M:
        print(*curr)
        return

    used = -1
    for i in range(start, len(nums)):
        if nums[i] != used:
            curr.append(nums[i])
            backtrack(i, curr)
            curr.pop()
            used = nums[i]

backtrack(0, [])
