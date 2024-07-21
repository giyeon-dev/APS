import sys

N, game_type = sys.stdin.readline().strip().split()
N = int(N)
ppl = set()
for _ in range(N):
    ppl.add(sys.stdin.readline().strip())

ans = 0
if game_type == 'Y':
    ans = len(ppl)

elif game_type == 'F':
    ans = len(ppl) // 2

elif game_type == 'O':
    ans = len(ppl) // 3


print(ans)