import sys
N = int(sys.stdin.readline().strip())
lst = [int(sys.stdin.readline().strip()) for _ in range(N)]

stack = []
cnt = 0
for i in range(N):
    curr = lst[i]

    while stack and curr >= stack[-1]:
        stack.pop()
    stack.append(curr)
    cnt += len(stack) - 1
    
print(cnt)

