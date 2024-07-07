import math
H, W, N, M = map(int, input().split())

row = math.ceil(H / (N + 1))
col = math.ceil(W / (M + 1))

mx_ppl = row * col

print(mx_ppl)
