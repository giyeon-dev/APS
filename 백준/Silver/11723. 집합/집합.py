import sys
N = int(sys.stdin.readline().strip())
S = set()
for _ in range(N):
    data = sys.stdin.readline().strip().split()

    if len(data) == 1:
        if data[0] == 'all':
            S = set([n for n in range(1, 21)])

        elif data[0] == 'empty':
            S = set()
    else:

        command = data[0]
        x = int(data[1])

        if command == 'add':
            S.add(x)

        elif command == 'remove':
            S.discard(x)

        elif command == 'check':
            if x in S:
                print(1)
            else:
                print(0)

        elif command == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
