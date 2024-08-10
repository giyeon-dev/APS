def plus(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return plus(n - 1) + plus(n - 2) + plus(n - 3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(plus(n))