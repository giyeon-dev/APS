from collections import deque

N, K = map(int, input().split())
mx = 10 ** 5
visited = [0] * (mx + 1)


def bfs(N):
    q = deque()
    q.append(N)

    while q:
        curr = q.popleft()
        if curr == K:
            return visited[curr]

        for next in (curr - 1, curr + 1, curr * 2):
            if 0 <= next <= mx and not visited[next]:
                visited[next] = visited[curr] + 1
                q.append(next)


print(bfs(N))