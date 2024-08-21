from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

def bfs(r, c, d):
    q = deque()
    q.append((r, c, d))
    cleaned = [[0] * M for _ in range(N)]
    cleaned[r][c] = 1

    cnt = 1

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        cr, cc, cd = q.popleft()
        check = False # 청소 공간 찾았는지 체크

        for i in range(4):
            nd = (cd + 3) % 4 # 반시계 방향 회전
            nr, nc = cr + directions[nd][0], cc + directions[nd][1]

            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 and cleaned[nr][nc] == 0:
                cleaned[nr][nc] = 1
                q.append(((nr, nc, nd)))
                cnt += 1
                check = True
                break

            cd = nd

        if not check: # 4방향 모두 청소 못할 때 후진
            bd = (cd + 2) % 4
            br, bc = cr + directions[bd][0], cc + directions[bd][1]

            if room[br][bc] == 0:
                q.append((br, bc, cd))
            else:
                break  #작동 종료

    print(cnt)

bfs(r,c,d)



