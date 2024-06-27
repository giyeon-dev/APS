import sys
input = sys.stdin.readline

queue = []
N = int(input().strip())
for tc in range(N):
    command = input().strip().split()

    if command[0] == 'push':
        queue.append(command[1])

    elif command[0] == 'pop':
        if queue:
            print(queue[0])
            queue.pop(0)
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(queue))

    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
