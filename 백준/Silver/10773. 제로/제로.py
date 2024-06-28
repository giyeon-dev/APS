import sys
K = int(sys.stdin.readline().strip())
lst =[int(sys.stdin.readline().strip()) for _ in range(K)]

stack = []

for n in lst:
    if n == 0:
        stack.pop()
    else:
        stack.append(n)


print(sum(stack))
