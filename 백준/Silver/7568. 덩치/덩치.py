N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x,y))

rank_lst = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                rank_lst[i] += 1

print(*rank_lst)