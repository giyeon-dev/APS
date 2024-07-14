import sys
import math
N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))
T, P = map(int, sys.stdin.readline().strip().split())

t_bundle = 0

for size in lst:
    t_bundle += math.ceil(size / T)

p_bundle = N // P
one = N % P

print(t_bundle)
print(p_bundle, one)