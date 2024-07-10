def solution(n, computers):
    ans = 0
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        
        for c in range(n):
            if computers[v][c] == 1 and not visited[c]:
                dfs(c)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1

    return ans