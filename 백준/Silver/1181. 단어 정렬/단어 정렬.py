import sys

N = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for _ in range(N)]

set_words = list(set(words))
set_words.sort()
set_words.sort(key=len)

for word in set_words:
    print(word)