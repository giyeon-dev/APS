T = int(input())

stack = []
ans = []
for tc in range(T):
    order = input().split()

    if order[0] == 'push':
        stack.append(order[-1])

    elif order[0] == 'pop':
        if stack:
           ans.append(stack[-1])
           stack.pop()
        else:
            ans.append(-1)

    elif order[0] == 'size':
        ans.append(len(stack))

    elif order[0] == 'empty':
        if stack:
            ans.append(0)
        else:
            ans.append(1)

    elif order[0] == 'top':
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)

for a in ans:
    print(a)