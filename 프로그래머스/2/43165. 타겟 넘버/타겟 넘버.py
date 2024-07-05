def solution(numbers, target):
    ans = 0
    total = sum(numbers)
    minus_nums = (total - target) // 2
    
    if minus_nums < 0:
        ans = 0
    elif minus_nums == 0:
        ans = 1
    else:
        def comb(nums):
            result = []
            def backtrack(start, curr):
                if sum(curr) == minus_nums:
                    result.append(curr[:])
                    return
            
                for i in range(start, len(nums)):
                    curr.append(nums[i])
                    backtrack(i + 1, curr)
                    curr.pop()
            backtrack(0, [])
            return len(result) 
        ans = comb(numbers)
    return ans
                
        