def solution(N, stages):
    ans = []
    player = len(stages)
    fail_player = 0
    fail_rate = {}
    stages.sort()
    
    for n in range(1, N + 1):
        if player == 0:
            fail_rate[n] = 0
           
        else:
            fail_player = stages.count(n)
            fail_rate[n] = fail_player/ player
            player -= fail_player
            
    
    
    sorted_dict = sorted(fail_rate.items(), key = lambda x: x[1], reverse = True)
    
    
    ans = [k for k, v in sorted_dict]
    
    return ans
            