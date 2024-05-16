def solution(cards1, cards2, goal):
    ans = ''
    
    while len(goal) > 0:
        if len(cards1) > 0 and goal[0] == cards1[0]:
            cards1.remove(cards1[0])
            goal.remove(goal[0])
            
        elif len(cards2) > 0 and goal[0] == cards2[0]:
            cards2.remove(cards2[0])
            goal.remove(goal[0])

        else:
            ans = 'No'
            break
    
    if len(goal) == 0:
        ans =  'Yes'
    else:
        ans = 'No'
            
    return ans