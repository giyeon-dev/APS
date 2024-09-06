S = input()
ans = set()

for start in range(len(S)):
    for end in range(start + 1, len(S)+1):
        ans.add(S[start : end])

print(len(ans))