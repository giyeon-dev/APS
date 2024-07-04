from collections import deque
N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

def maze(N, M, matrix):
    visited = [[False] * M for _ in range(N)]

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        visited[r][c] = True
        # 상 하 좌 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            cur_r, cur_c = q.popleft()

            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]

                # 범위 안에 있는 경우
                if  next_r >= 0 and next_r < N and next_c >= 0 and next_c < M:
                    if matrix[next_r][next_c] == 1 and not visited[next_r][next_c]:
                        q.append((next_r, next_c))
                        visited[next_r][next_c] = True
                        matrix[next_r][next_c] = matrix[cur_r][cur_c] + 1

    bfs(0, 0)

    return matrix[N-1][M-1]

print(maze(N, M, matrix))