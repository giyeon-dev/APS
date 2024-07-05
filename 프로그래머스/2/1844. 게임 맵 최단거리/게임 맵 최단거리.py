from collections import deque
def solution(maps):

    row = len(maps)
    col = len(maps[0])
    visited = [[False]*col for _ in range(row)]
    distance = [[0]*col for _ in range(row)] # 경로 저장 배열

    q = deque()
    q.append((0,0))
    visited[0][0] = True
    distance[0][0] = 1
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        cur_r, cur_c = q.popleft()

        for dr, dc in directions:
            next_r = cur_r + dr
            next_c = cur_c + dc
            # 범위 체크
            if  0 <= next_r < row and 0 <= next_c < col:
                if maps[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = True
                    distance[next_r][next_c] = distance[cur_r][cur_c] + 1

                    if next_r == row - 1 and next_c == col - 1:
                        return distance[next_r][next_c]

    
    return -1