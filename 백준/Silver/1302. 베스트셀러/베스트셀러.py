import sys
n = int(sys.stdin.readline().strip())
book_dict = dict()
for _ in range(n):
    book = sys.stdin.readline().strip()

    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1

mx = max(book_dict.values())

for i, v in sorted(book_dict.items()):
    if v == mx:
        print(i)
        break