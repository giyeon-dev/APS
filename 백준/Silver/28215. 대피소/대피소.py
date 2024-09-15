import sys
from itertools import combinations
N, K = map(int, sys.stdin.readline().strip().split())

homes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

comb = combinations(homes, K)

min_distance = float('INF')

for shelters in comb:
    max_distance = 0
    for home in homes:
        # 각 집에 대해 가장 가까운 피난처까지의 거리
        min_home_distance = float('INF')
        for shelter in shelters:
            min_home_distance = min(min_home_distance, distance(shelter[0], shelter[1], home[0], home[1]))

        # 가장 가까운 피난처 거리 중 최대값
        max_distance = max(max_distance, min_home_distance)
    
    # 최대 거리 중 최소값
    min_distance = min(min_distance, max_distance)

print(min_distance)

