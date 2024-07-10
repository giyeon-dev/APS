import math
from itertools import permutations

def solution(numbers):
    
    # 소수 판별 함수
    def prime_num(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    # 가능한 숫자 조합
    num_lst = []
    lst = list(numbers)
    for i in range(1, len(numbers) + 1):
        num_lst += (list(permutations(lst, i)))
    
    ans_lst = set([int("".join(num)) for num in num_lst])
    
    # 숫자 소수 판별
    cnt = 0
    for n in ans_lst:
        if prime_num(n):
            cnt += 1
   
    return cnt