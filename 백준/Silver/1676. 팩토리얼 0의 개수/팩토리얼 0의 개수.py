N = int(input())
def factorial(n):
    if n == 0:
        return 1

    return factorial(n - 1) * n

s = str(factorial(N))
cnt = 0
for letter in s[::-1]:
    if letter == '0':
        cnt += 1
    else:
        break

print(cnt)
