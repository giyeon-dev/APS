'''
큰 직사각형 넓이에서 작은 직사각형 넓이 빼기
가로 - 1, 2 / 세로 - 3, 4
큰 직사각형
- 가장 긴 가로와 가장 긴 세로
작은 직사각형
- 세로: 가장 긴 가로 변 양쪽의 두개 세로 변의 차이
- 가로: 가장 긴 세로 변 양쪽의 두개 가로 변의 차이

'''

K = int(input())
dir_len = [tuple(map(int, input().split())) for _ in range(6)]

# 큰 직사각형 넓이 구하기
big_w = big_h = 0
big_w_idx = big_h_idx = -1

for i in range(6):
    direction, length = dir_len[i]

    if direction == 1 or direction == 2:
        if length > big_w:
            big_w = length
            big_w_idx = i

    elif direction == 3 or direction == 4:
        if length > big_h:
            big_h = length
            big_h_idx = i

# 작은 직사각형 넓이(가장 긴 변 앞 뒤 인덱스 길이 차이)
small_w = abs(dir_len[(big_h_idx - 1) % 6][1] - dir_len[(big_h_idx + 1) % 6][1] )
small_h = abs(dir_len[(big_w_idx - 1) % 6][1] - dir_len[(big_w_idx + 1) % 6][1] )

big = big_w * big_h
small = small_w * small_h

ans = (big - small) * K

print(ans)