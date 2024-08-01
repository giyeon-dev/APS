A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

dict = {}
for n in result:
    if (ord(n) - 48) in dict:
        dict[ord(n) - 48] += 1
    else:
        dict[ord(n) - 48] = 1


for i in range(10):
    if i not in dict:
        print(0)
    else:
        print(dict[i])