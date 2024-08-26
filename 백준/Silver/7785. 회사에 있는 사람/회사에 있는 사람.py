n = int(input())
log = dict()

for _ in range(n):
    name, record = input().split()

    if record == 'enter':
        log[name] = True
    elif record == 'leave':
        if name in log:
            del log[name]

log = sorted(log.keys(), reverse=True)

for ppl in log:
    print(ppl)