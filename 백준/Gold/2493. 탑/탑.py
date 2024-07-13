import sys
N = int(sys.stdin.readline().strip())
tops = list(map(int, sys.stdin.readline().strip().split()))


lst = [0] * N
stack = []

for i in range(N):
    while stack and stack[-1][1] <= tops[i]: # 수신할 수 없는 탑 제거
        stack.pop() 

    if stack:
        lst[i] = stack[-1][0] + 1

    stack.append((i, tops[i]))


print(*lst)




