n = int(input())


cnt = 0
for num in range(1, n + 1):
    # 한자리 또는 두자리 수
    if num < 100:
        cnt += 1

    # 세자리 수
    else:
        a = num // 100
        b = (num // 10) % 10
        c = num % 10

        if (b - a) == (c - b):
            cnt += 1

print(cnt)
