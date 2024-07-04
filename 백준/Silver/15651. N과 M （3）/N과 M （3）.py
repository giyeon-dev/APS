N, M = map(int, input().split())

def permutations(N, M):
    ans = []
    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return

        for n in range(1, N + 1):
            curr.append(n)
            backtrack(curr)
            curr.pop()

    backtrack([])
    return ans

result = permutations(N, M)

for i in range(len(result)):
    print(*result[i])