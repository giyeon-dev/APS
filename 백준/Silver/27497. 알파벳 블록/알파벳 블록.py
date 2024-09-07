import sys
N = int(sys.stdin.readline().strip())
from collections import deque

deq = deque()
stack = [] # 가장 나중에 추가된 블록 체크하기 위한 스택
for _ in range(N):
    button = sys.stdin.readline().strip().split()

    if button[0] == '1':
        deq.append(button[1])
        stack.append('R')

    elif button[0] == '2':
        deq.appendleft(button[1])
        stack.append('L')
    elif button[0] == '3':
        if stack:
            last = stack.pop()
            if last == 'R':
                deq.pop()
            else:
                deq.popleft()

if deq:
    print(''.join(deq))
else:
    print(0)