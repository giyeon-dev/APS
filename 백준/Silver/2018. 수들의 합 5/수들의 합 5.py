n = int(input())

start = 1
end = 1
cur_sum = 1
cnt = 0

while start <= n:
    if cur_sum == n:
        cnt += 1
        cur_sum -= start # 구간의 시작 지점 이동
        start += 1

    elif cur_sum < n: # 구간 합이 n보다 작은 경우 끝 구간 확장
        end += 1
        cur_sum += end

    else: # 구간 합이 n보다 큰 경우 앞 구간 축소
        cur_sum -= start
        start += 1

print(cnt)