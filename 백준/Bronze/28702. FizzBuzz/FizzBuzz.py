lst = [input() for _ in range(3)]

target = 0
target_idx = 0
ans = 0
for idx, n in enumerate(lst):
    if n != 'Fizz' and n != 'Buzz' and n != 'FizzBuzz':
        target = int(n)
        target_idx = idx

if target_idx == 0:
    ans = target + 3
elif target_idx == 1:
    ans = target + 2
else:
    ans = target + 1

if ans % 3 == 0 and ans % 5 == 0:
    ans = 'FizzBuzz'
elif ans % 3 == 0 and ans % 5 != 0:
    ans = 'Fizz'
elif ans % 3 != 0 and ans % 5 == 0:
    ans = 'Buzz'

print(ans)