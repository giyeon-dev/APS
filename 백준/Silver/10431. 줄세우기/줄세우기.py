import sys
T = int(sys.stdin.readline().strip())

for tc in range(1, T + 1):
    lst = list(map(int, sys.stdin.readline().strip().split()))
    lst = lst[1:]

    cnt = 0
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp

                cnt += 1

    print(f'{tc} {cnt}')