from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

candidates = list(combinations(chickens, M))

def get_distance(candidate):
    result = 0
    for hr, hc in houses:
        temp = 999999

        for cr, cc in candidate:
            temp = min(temp, abs(hr - cr) + abs(hc - cc))
        result += temp

    return result

ans = 999999
for candidate in candidates:
    ans = min(ans, get_distance(candidate))

print(ans)