import sys
N, M = map(int, sys.stdin.readline().strip().split())
lst = list(map(int,sys.stdin.readline().strip().split()))

# 누적 합 활용
prefix_sum = [0] * N
prefix_sum[0] = lst[0]
for n in range(1, N):
    prefix_sum[n] = prefix_sum[n-1] + lst[n]


for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())

    start_idx = i - 1
    end_idx = j - 1

    if start_idx == 0:
        ans = prefix_sum[end_idx]
    else:
        ans = prefix_sum[end_idx] - prefix_sum[start_idx - 1]
        
    print(ans)