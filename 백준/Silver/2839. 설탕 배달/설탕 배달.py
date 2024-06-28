N = int(input())

bag5 = N // 5
ans = -1
for bag in range(bag5, -1, -1):
    if (N - bag * 5) % 3 == 0:
        bag3 = (N - bag * 5) // 3
        ans = bag + bag3
        break

print(ans)



