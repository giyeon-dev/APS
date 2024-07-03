import sys
input = sys.stdin.readline
N = int(input())

lst = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    lst.append((x, y))

lst.sort(key=lambda lst: (lst[1], lst[0]))

for x, y in lst:
    print(x, y)