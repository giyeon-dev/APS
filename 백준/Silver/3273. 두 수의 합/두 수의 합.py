n = int(input())
lst = sorted(list(map(int, input().split())))
x = int(input())

left, right = 0, len(lst) - 1
cnt = 0
while left < right:
    curr = lst[left] + lst[right]

    if curr == x:
        cnt += 1
        left += 1
        right -= 1

    elif curr < x:
        left += 1

    else:
        right -= 1

print(cnt)