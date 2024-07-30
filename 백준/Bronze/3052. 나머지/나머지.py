lst = [int(input()) for _ in range(10)]

ans_set = set()

for n in lst:
    remain = n % 42
    ans_set.add(remain)

print(len(ans_set))