from functools import cmp_to_key

def compare(a, b):

    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    nums = list(map(str, numbers))
    
    
    nums.sort(key=cmp_to_key(compare))
    
    result = ''.join(nums)
    
    
    return str(int(result))

