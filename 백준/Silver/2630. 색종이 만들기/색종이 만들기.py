n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def check_color(paper, x, y, n):

    color = paper[x][y]
    for r in range(x, x + n):
        for c in range(y, y + n):
            if paper[r][c] != color:
                return False
    return True

def count_paper(paper, x, y, n):
    global white, blue
    if check_color(paper, x, y, n):
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        count_paper(paper, x, y, half)
        count_paper(paper, x, y + half, half)
        count_paper(paper, x + half, y, half)
        count_paper(paper, x + half, y + half, half)

count_paper(paper, 0, 0, n)
print(white)
print(blue)