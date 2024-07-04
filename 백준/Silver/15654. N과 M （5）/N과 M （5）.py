import sys

N, M = map(int, sys.stdin.readline().strip().split())
lst = sorted(list(map(int, sys.stdin.readline().strip().split())))

def permutations(M, lst):
    ans = []

    def backtrack(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return

        for n in lst:
            if n not in curr:
                curr.append(n)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return ans

result = permutations(M, lst)

for i in range(len(result)):
    print(*result[i])