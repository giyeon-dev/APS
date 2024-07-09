n = int(input())
def make_rectangle(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            a = i
            b = n // i
            if (a, b) not in lst and (b, a) not in lst:
                lst.append((a, b))
    return lst


cnt = 0
for k in range(1, n + 1):
    rect = make_rectangle(k)
    cnt += len(rect)

print(cnt)