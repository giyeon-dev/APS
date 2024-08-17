import sys
from collections import deque

N = int(sys.stdin.readline().strip())
q = deque()
for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'push':
        (q.append(command[1]))

    elif command[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
