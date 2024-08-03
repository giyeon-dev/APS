N = int(input())
cookie = [list(map(str, input())) for _ in range(N)]

# 심장 위치
def find_heart(cookie, N):
    for r in range(N):
        for c in range(N):
            if cookie[r][c] == '*':
                return r + 1, c

heart_r, heart_c = find_heart(cookie, N)

# 팔 길이
def arm_length(cookie, N):
    left_arm = right_arm = 0
    for r in range(N):
        for c in range(N):
            if r == heart_r and c < heart_c:
                if cookie[r][c] == '*':
                    left_arm += 1

            if r == heart_r and c > heart_c:
                if cookie[r][c] == '*':
                    right_arm += 1
    return left_arm, right_arm

# 허리 길이
def waist_length(cookie, N):
    waist = 0
    for r in range(N):
        for c in range(N):
            if r > heart_r and c == heart_c:
                if cookie[r][c] == '*':
                    waist += 1
    return waist

waist = waist_length(cookie, N)
waist_r, waist_c = heart_r + waist, heart_c

# 다리 길이
def leg_length(cookie, N):
    left_leg = right_leg = 0
    for r in range(N):
        for c in range(N):
            if r >= waist_r + 1 and c == waist_c - 1:
                if cookie[r][c] == '*':
                    left_leg += 1

            if r >= waist_r + 1 and c == waist_c + 1:
                if cookie[r][c] == '*':
                    right_leg += 1
    return left_leg, right_leg

arm = arm_length(cookie, N)
leg = leg_length(cookie, N)

print(heart_r + 1, heart_c + 1)
print(*arm, waist, *leg)