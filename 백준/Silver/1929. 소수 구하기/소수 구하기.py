
M, N = map(int, input().split())

def sieve_of_eratosthenes(m, n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False

    for i in range(m, n+1):
        if prime[i]:
            print(i)

sieve_of_eratosthenes(M,N)