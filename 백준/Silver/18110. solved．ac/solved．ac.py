import sys
n = int(sys.stdin.readline().strip())
lst = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])


# 파이썬 내장 round 함수는 5에서 반올림 할 경우 앞 지리가 홀수면 올림, 짝수면 내림
def num_round(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


num = num_round(n * 0.15)

include_lst = lst[num: n - num]

ans = 0
if lst == 0:
    ans = 0
else:
    if len(include_lst) > 0:
        ans = num_round(sum(include_lst) / len(include_lst))

print(ans)