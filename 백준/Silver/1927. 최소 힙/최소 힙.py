import heapq
import sys

n = int(sys.stdin.readline().strip())

heap = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())

    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)