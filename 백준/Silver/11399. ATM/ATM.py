N = int(input())
lst = sorted(list(map(int, input().split())))

ans = 0

for i in range(len(lst)):
    ans += lst[i] * (len(lst) - i)

print(ans)