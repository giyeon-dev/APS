def solution(board, h, w):
    ans = 0
    n = len(board)
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    
    for dr, dc in directions:  
        nr = h + dr
        nc = w + dc

        if 0 <= nr < n and 0 <= nc < n:
            if board[h][w] == board[nr][nc]:
                ans += 1
    
    return ans