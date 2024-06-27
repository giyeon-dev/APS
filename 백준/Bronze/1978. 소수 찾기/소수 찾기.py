import math
N = int(input())
nums = list(map(int, input().split()))

def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

ans = sum(1 for n in nums if isPrime(n))

print(ans)