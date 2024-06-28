from collections import deque
N, K = map(int, input().split())
def josephus(N, K):
    deq = deque([n for n in range(1, N + 1)])

    lst = []
    while deq:
        deq.rotate(-(K-1))
        lst.append(deq.popleft())

    return lst

ans = josephus(N, K)
print(f"<{', '.join(map(str, ans))}>")

