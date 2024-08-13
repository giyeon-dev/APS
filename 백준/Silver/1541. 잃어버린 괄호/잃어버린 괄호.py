S = input().split('-')

ans = 0
first = S[0]

for i in first.split('+'):
    ans += int(i)

for part in S[1:]:
    for j in part.split('+'):
        ans -= int(j)

print(ans)
