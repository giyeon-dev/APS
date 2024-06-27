import sys
input = sys.stdin.readline
N = int(input().strip())

points = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    points.append((x,y))

points.sort()

for point in points:
    print(point[0], point[1])