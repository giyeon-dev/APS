import sys

N = int(sys.stdin.readline().strip())
lst = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().strip().split())
    lst.append((start, end))

lst.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간이 빠른 기준으로 정렬

cnt = 0
end_time = 0
for start, end in lst:
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)