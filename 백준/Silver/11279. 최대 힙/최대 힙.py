import sys
import heapq

N = int(sys.stdin.readline().strip())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())

    if x == 0:
        if heap:
            print(-heapq.heappop(heap)) # 최대값 출력
        else:
            print(0)
    else:
        heapq.heappush(heap, -x) # 값 추가