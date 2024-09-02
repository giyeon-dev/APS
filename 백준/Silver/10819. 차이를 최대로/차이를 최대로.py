from itertools import permutations
n = int(input())
lst = list(map(int, input().split()))

ans = -999999
for perm in permutations(lst):
    total = 0
    for i in range(1, n):
        total += abs(perm[i-1] - perm[i])

    if total > ans:
        ans = total

print(ans)