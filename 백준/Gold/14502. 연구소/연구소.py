from itertools import combinations
from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 벽 세울 수 있는 모든 조합 구하기
empty_lst = []
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 0:
            empty_lst.append((r, c))

walls_comb = list(combinations(empty_lst, 3))


# 바이러스 위치
virus = []
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 2:
            virus.append((r, c))

def bfs(new_matrix):
    q = deque(virus)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        cr, cc = q.popleft()
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and new_matrix[nr][nc] == 0:
                new_matrix[nr][nc] = 2
                q.append((nr, nc))


# 안전 영역
def safety(matrix):
    cnt = 0
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 0:
                cnt += 1
    return cnt

# 안전 영역 최대값
max_safety_cnt = 0
for walls in walls_comb:
    new_matrix = deepcopy(matrix)
    for r, c in walls:
        new_matrix[r][c] = 1
    bfs(new_matrix)
    safety_cnt = safety(new_matrix)
    max_safety_cnt = max(max_safety_cnt, safety_cnt)

print(max_safety_cnt)