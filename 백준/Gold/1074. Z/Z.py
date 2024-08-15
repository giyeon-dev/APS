N, r, c = map(int, input().split())

def z_search(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    if r < half and c < half:
        return z_search(n - 1, r, c)

    elif r < half and c >= half:
        return half * half + z_search(n - 1, r, c - half)

    elif r >= half and c < half:
        return 2 * half * half + z_search(n - 1, r - half, c)

    else:
        return 3 * half * half + z_search(n - 1, r - half, c - half)


print(z_search(N, r, c))