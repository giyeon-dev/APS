def solution(n, m=1234567):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, (a + b) % m
        return b