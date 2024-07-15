import sys
n = int(sys.stdin.readline().strip())
target = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []
ans = []
curr = 1
possible = True

for num in target:
    while curr <= num:
        stack.append(curr)
        ans.append('+')
        curr += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        possible = False
        break

if possible:
    for a in ans:
        print(a)
else:
    print("NO")