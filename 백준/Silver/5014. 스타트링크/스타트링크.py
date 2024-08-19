import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().strip().split())
visited = [-1 for _ in range(F + 1)]

def bfs():
    q = deque()
    q.append(S)
    visited[S] = 0

    while q:
        curr = q.popleft()

        if curr == G:
            return visited[curr]
        else:
            for next in (curr + U, curr - D):
                if ( 0< next <= F) and visited[next] == -1:
                    visited[next] = visited[curr] + 1
                    q.append(next)

    return "use the stairs"

print(bfs())