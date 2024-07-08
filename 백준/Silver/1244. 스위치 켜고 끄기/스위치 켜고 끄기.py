N = int(input())
lst = list(map(int, input().split()))
T = int(input())
for _ in range(T):
    WM, num = map(int, input().split())

    if WM == 1:
        num_lst = []
        for n in range(1, len(lst) + 1):
            if n % num == 0:
                num_lst.append(n)

        for n in num_lst:
            if lst[n - 1] == 1:
                lst[n - 1] = 0
            else:
                lst[n - 1] = 1

    else:
        idx = num - 1
        left, right = idx - 1, idx + 1
        if lst[idx] == 1:
            lst[idx] = 0
        else:
            lst[idx] = 1

        while left >= 0 and right <= len(lst) - 1:

            if lst[left] == lst[right]:
                if lst[left] == 1:
                    lst[left] = 0
                else:
                    lst[left] = 1

                if lst[right] == 1:
                    lst[right] = 0
                else:
                    lst[right] = 1

                left -= 1
                right += 1

            else:
                break

line = 20

for i in range(0, len(lst), line):
    print(*lst[i: i + line])

