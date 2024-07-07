def is_triangle(a, b, c):
    ans = []
    if a == 0 and b == 0 and c == 0:
        return 'end'

    mx = max(a, b, c)
    if mx < (a + b + c) - mx:

        if a == b == c:
            return 'Equilateral'
        elif a == b or a == c or b == c:
            return 'Isosceles'
        else:
            return 'Scalene'

    else:
        return 'Invalid'

while True:
    a, b, c = map(int, input().split())
    ans = is_triangle(a, b, c)
    if ans == 'end':
        break
    print(ans)