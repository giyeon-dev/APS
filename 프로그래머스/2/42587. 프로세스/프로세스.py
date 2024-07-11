from collections import deque
def solution(priorities, location):
    deq = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    
    order = 0
    while deq:
        q = deq.popleft()
        has_priority = False
        
        for i, p in deq:
            if q[1] < p:
                has_priority = True
                break
                
        if has_priority:
            deq.append(q)
        else:
            order += 1
        
            if q[0] == location:
                return order