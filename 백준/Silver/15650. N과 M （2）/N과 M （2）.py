N, M = map(int, input().split())

def n_and_m(N, M):
    lst = []
    def backtracking(start, curr):
        if len(curr) == M:
            if sorted(curr) in lst:
                return
            else:
                lst.append(curr[:])
            return

        for n in range(start, N + 1):
            if n not in curr:
                curr.append(n)
                backtracking(start + 1, curr)
                curr.pop()

    backtracking(1, [])
    return lst

ans = n_and_m(N, M)

for a in ans:
    print(*a)



