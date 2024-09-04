A = [list(map(int, input().split())) for _ in range(5)]
B = [list(map(int, input().split())) for _ in range(5)]


work_load = [0] * 5
for x in range(5):
    for y in range(5):
        for i in range(5):
            work_load[x] += A[x][i] * B[i][y]

min_work = min(work_load)
ppl = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]

for i in range(4, -1, -1): # 우선순위 반대
    if work_load[i] == min_work:
        print(ppl[i])
        break




