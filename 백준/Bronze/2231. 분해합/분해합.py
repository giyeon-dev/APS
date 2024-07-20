N = int(input())
# 분해합
def hap(N):
    return N + sum(map(int, str(N)))

found = False
for n in range(1, N):

    if hap(n) == N:
        print(n)
        found = True
        break
        
if not found:
    print(0)