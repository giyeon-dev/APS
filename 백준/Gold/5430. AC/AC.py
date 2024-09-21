import sys
from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    lst = deque(sys.stdin.readline().strip()[1:-1].split(","))
    deq = deque(lst)

    if n == 0:
        deq = deque()

    reverse = False
    error = False

    for command in p:
        if command == 'R':
            reverse = not reverse

        elif command == 'D':
            if not deq:
                print('error')
                error = True
                break

            if reverse:
                deq.pop()
            else:
                deq.popleft()

    if not error:
        if reverse:
            deq.reverse()
        print('[' + ','.join(deq) + ']')

