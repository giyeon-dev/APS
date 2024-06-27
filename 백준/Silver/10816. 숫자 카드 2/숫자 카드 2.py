import sys
input = sys.stdin.readline

N = int(input().strip())
n_lst = sorted(list(map(int, input().strip().split())))
M = int(input().strip())
m_lst = list(map(int, input().strip().split()))

# 숫자 카드 개수 dict
n_dict = {}
for n in n_lst:
    if n in n_dict:
        n_dict[n] += 1
    else:
        n_dict[n] = 1

# 이진 탐색
def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return True

        elif lst[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return False

ans = []
for m in m_lst:
    if binary_search(n_lst, m):
        ans.append(n_dict[m])
    else:
        ans.append(0)

for a in ans:
    print(a, end=' ')