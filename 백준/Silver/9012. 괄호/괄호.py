T = int(input())
for tc in range(T):
    ps = input()

    stack = []
    vps = True
    for p in ps:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                vps = False
                break

    if vps and not stack:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)