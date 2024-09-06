import sys
n = int(sys.stdin.readline().strip())
count_dict = dict()
for _ in range(n):
    letter = sys.stdin.readline().strip().split('.')
    extension = letter[1]

    if extension in count_dict:
        count_dict[extension] += 1
    else:
        count_dict[extension] = 1

for i, v in sorted(count_dict.items()):
    print(i, v)