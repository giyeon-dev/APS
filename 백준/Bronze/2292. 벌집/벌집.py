N = int(input())
def find_layers(N):
    if N == 1:
        return 1

    layer = 1
    current = 1 # 각 layer의 최대 숫자

    while current < N:
        current += 6 * layer # 각 layer마다 6의 배수씩 증가
        layer += 1

    return layer

print(find_layers(N))