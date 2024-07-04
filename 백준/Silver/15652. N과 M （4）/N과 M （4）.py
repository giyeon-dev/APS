N, M = map(int, input().split())

def combinations(N, M):
    ans = []
    def backtrack(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return

        for n in range(start, N + 1):
            curr.append(n)
            backtrack(n, curr)
            curr.pop()

    backtrack(1, [])
    return ans

result = combinations(N, M)

for i in range(len(result)):
    print(*result[i])