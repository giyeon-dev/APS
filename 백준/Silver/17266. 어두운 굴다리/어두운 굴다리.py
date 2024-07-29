import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))

start = lst[0]
end = N - lst[-1]
height = max(start, end)

for i in range(len(lst) - 1):
    gap = (lst[i + 1] - lst[i])

    if gap % 2 == 0:
        gap = gap // 2
    else:
        gap = gap // 2 + 1

    if gap > height:
        height = gap


print(height)