import sys
input = sys.stdin.readline
N = int(input().strip())

members = []

for idx in range(N):
    age, name = input().strip().split()
    members.append((int(age), name, idx))

members.sort(key=lambda x: (x[0], x[2]))

for member in members:
    print(member[0], member[1])