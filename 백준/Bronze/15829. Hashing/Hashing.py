N = int(input())
lst = list(input())

ans = 0
for i in range(N):
    ans += (ord(lst[i]) - 96) * (31 ** i)

    ans = ans % 1234567891

print(ans)