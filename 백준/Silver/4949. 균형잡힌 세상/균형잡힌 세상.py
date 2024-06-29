import sys

while True:
    s = sys.stdin.readline().rstrip()
    stack = []

    if s == '.':
        break

    balanced = True
    for letter in s:

        if letter == '(' or letter == '[':
            stack.append(letter)

        elif letter == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            else:
                stack.pop()

        elif letter == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            else:
                stack.pop()

    if not stack and balanced:
        print('yes')
    else:
        print('no')


