S = input()

ans = []
stack = []
is_tag = False

for char in S:
    if char == '<':
        while stack: # 스택에 쌓인 단어 뒤집어서 추가
            ans.append(stack.pop())
        ans.append(char)
        is_tag = True

    elif char == '>':
        ans.append(char)
        is_tag = False

    elif is_tag:
        ans.append(char)

    elif char == ' ':
        while stack:
            ans.append(stack.pop())
        ans.append(char)

    else:
        stack.append(char)

# 마지막 단어 체크
while stack:
    ans.append(stack.pop())

print(''.join(ans))