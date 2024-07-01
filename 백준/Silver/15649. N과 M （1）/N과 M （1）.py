N, M = map(int, input().split())


def n_and_m(N, M):
    lst = []
    def backtracking(curr):
        if len(curr) == M:
            lst.append(curr[:])
            return

        for n in range(1, N + 1):
            if n not in curr:
                curr.append(n)
                backtracking(curr)
                curr.pop()

    backtracking([])
    return lst

ans = n_and_m(N, M)

for a in ans:
    print(*a)



