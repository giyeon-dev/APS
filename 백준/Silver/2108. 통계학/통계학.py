import sys
N = int(sys.stdin.readline().strip())
lst = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

def mean(lst):
    return round((sum(lst) / len(lst)))

def median(lst):
    N = len(lst)
    idx = N // 2

    if N % 2 == 0:
        return (lst[idx - 1] + lst[idx]) / 2
    else:
        return lst[idx]

def mode(lst):
    dict = {}

    for n in lst:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    mx = max(dict.values())

    candidates = []
    for n, freq in dict.items():
        if freq == mx:
            candidates.append(n)

    if len(candidates) > 1:
        return sorted(candidates)[1]
    else:
        return candidates[0]

def scale(lst):
    return max(lst) - min(lst)


print(mean(lst))
print(median(lst))
print(mode(lst))
print(scale(lst))