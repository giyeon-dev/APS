N = int(input())
budget = sorted(list(map(int, input().split())))
M = int(input())

low, high = 0, max(budget)
ans = 0
while low <= high:
    mid = (low + high) // 2
    total = 0
    for n in budget:
        if n > mid:
            total += mid
        else:
            total += n

    if total <= M:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)

