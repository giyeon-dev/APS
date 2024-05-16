# 소수 판별 함수

def prime(n):
    
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def solution(nums):
    ans = 0
    
    # 모든 조합 구하기
    pick_three = []
    three_sum = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                three_sum = nums[i] + nums[j] + nums[k]
                if prime(three_sum):
                    pick_three.append(three_sum)
                    
    ans = len(pick_three)
                

    return ans