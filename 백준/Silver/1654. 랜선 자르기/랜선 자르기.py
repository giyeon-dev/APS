import sys
K, N = map(int, sys.stdin.readline().strip().split())
lst = [int(sys.stdin.readline().strip()) for _ in range(K)]

def lan(K, N, lst):
    # 이분탐색 초기값
    left = 1
    right = max(lst)
    lst.sort()

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for l in lst:
            total += (l // mid)

        if total >= N:
            ans = mid
            left = mid + 1 # 더 긴 랜선 시도
        else:
            right = mid - 1

    return ans

print(lan(K, N, lst))