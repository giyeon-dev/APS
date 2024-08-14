T = int(input())
for _ in range(T):
    N = int(input())

    dict = {}
    for _ in range(N):
        clothes, type = input().split()

        if type in dict:
            dict[type].append(clothes)
        else:
            dict[type] = [clothes]

    comb = 1
    for type in dict:
        comb *= (len(dict[type]) + 1) # +1은 해당 의상 선택 안하는 경우

    comb -= 1 # 모두 선택 안하는 경우 제외

    print(comb)