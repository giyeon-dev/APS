S = input()

dict = {}
for i in range(26):
    dict[chr(97 + i)] = -1

for idx, letter in enumerate(S):
    if dict[letter] != -1:
        continue
    if letter in dict:
        dict[letter] = idx


print(*dict.values())