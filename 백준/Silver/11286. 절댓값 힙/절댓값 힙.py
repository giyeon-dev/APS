import heapq
import sys

n = int(sys.stdin.readline().strip())

heap = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)