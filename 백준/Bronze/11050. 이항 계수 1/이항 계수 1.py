N, K = map(int, input().split())

# 이항 계수: n개 원소에서 k개 선택
# nCk = n!/k!(n-k)!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

ans = factorial(N) // (factorial(K) * factorial(N - K))

print(ans)