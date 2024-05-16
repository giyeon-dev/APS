def solution(nums):
    ans = 0
    
    # 폰켓몬 종류
    pocket_type = len(set(nums))
    
    # 선택 가능 개수
    max_num = len(nums) / 2
    
    '''
    선택 가능한 종류의 최대값
    (1)종류가 선택 가능 개수보다 많은 경우, 선택 가능 개수가 최대값
    (2)종류가 선택 가능 개수보다 작거나 같은 경우, 종류가 최대값
    '''
    
    ans = min(pocket_type, max_num)
    return ans