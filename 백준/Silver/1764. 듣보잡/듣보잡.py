import sys

never_seen = set()
never_heard = set()
N, M = map(int, sys.stdin.readline().strip().split())

for n in range(N):
    n = sys.stdin.readline().strip()
    never_seen.add(n)

for m in range(M):
    m = sys.stdin.readline().strip()
    never_heard.add(m)

ans = sorted(never_heard & never_seen)

print(len(ans))
for a in ans:
    print(a)