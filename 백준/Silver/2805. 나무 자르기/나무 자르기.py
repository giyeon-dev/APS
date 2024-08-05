import sys
N, M = map(int, sys.stdin.readline().strip().split())
tree = sorted(list(map(int, sys.stdin.readline().strip().split())))


start, end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2
    take_home = 0

    for t in tree:
        if t >= mid:
            take_home += (t - mid)

    if take_home >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)