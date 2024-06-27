import sys

def is_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    return False

while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())

    if a == 0 and b == 0 and c == 0:
        break

    if is_triangle(a, b, c):
        print("right")
    else:
        print("wrong")