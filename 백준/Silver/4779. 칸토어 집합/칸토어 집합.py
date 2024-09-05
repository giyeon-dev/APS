def cantor(n):
    if n == 1:
        return "-"
    else:
        left = cantor(n // 3)
        return left + " " * len(left) + left

while True:
    try:
        N = int(input())
        ans = cantor(3 ** N)
        print(ans)
    except EOFError:
        break