N = int(input())
pattern = input()

prefix, suffix = pattern.split('*')

for _ in range(N):
    word = input()

    if len(word) < len(prefix) + len(suffix):
        print("NE")
        continue


    if word.startswith(prefix) and word.endswith(suffix):
        print("DA")
    else:
        print("NE")