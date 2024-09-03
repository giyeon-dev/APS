N, M = map(int, input().split())
dict = dict()
for _ in range(N):
    team = input()
    member_cnt = int(input())
    dict[team] = []

    for _ in range(member_cnt):
        member = input()
        dict[team].append(member)

for _ in range(M):
    quiz = input()
    type = int(input())

    if type == 0:
        for mem in sorted(dict[quiz]):
            print(mem)

    elif type == 1:
        for key, values in dict.items():
            if quiz in values:
                print(key)
