A, B, V = map(int, input().split())

def snail(A, B, V):
    days = (V - B) / (A - B)
    if days == int(days):
        return int(days)
    else:
        return int(days) + 1
ans = snail(A, B, V)

print(ans)