N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]


def repaint(N, M, board):
    ans = []
    for r in range(N - 7):
        for c in range(M - 7):
            white = 0 # 시작점이 W인 패턴인 경우 다시 칠해야 하는 숫자 카운트
            black = 0 # 시작점이 검은색인 패턴인 경우 다시 칠해야 하는 숫자 카운트
            for i in range(r, r + 8):
                for j in range(c, c + 8):
                    if (i + j) % 2 == 0:
                        if board[i][j] != 'W':
                            white += 1
                        else:
                            black += 1
                    else:
                        if board[i][j] != 'B':
                            white += 1
                        else:
                            black += 1
                            
            ans.append(min(white, black)) # 두 패턴 중 최소값
    return min(ans)

print(repaint(N, M, board))