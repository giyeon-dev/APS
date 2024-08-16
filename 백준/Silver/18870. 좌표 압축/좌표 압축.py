import sys
n = int(sys.stdin.readline().strip())
lst = (list(map(int, input().split())))

set_lst = sorted(set(lst))

dict = {set_lst[i]: i for i in range(len(set_lst))}

for i in lst:
    print(dict[i], end=" ")