'''
같은 문자가 두 번 연속 나와서 짝을 지어야 함
모든 문자가 제거 되는지 확인
스택 활용해서 연속된 쌍 제거
'''
import sys
N = int(sys.stdin.readline().strip())
ans = 0
for _ in range(N):
    word = sys.stdin.readline().strip()

    stack = []
    for char in word:
        if stack and stack[-1] == char: # 스택이 비어있지 않고 스택 위의 문자와 같은 경우 제거
            stack.pop()
        else:
            stack.append(char) # 아닌 경우 문자 추가

    if not stack: # 스택이 비어있는 경우 좋은 단어
        ans += 1

print(ans)