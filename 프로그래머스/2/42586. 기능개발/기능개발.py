import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    
    days = deque()
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i]) / speeds[i]))
    
    
    mx_day = 0
    while days:
        day = days.popleft()
        
        if day > mx_day:
            answer.append(1)
            mx_day = day
        else:
            answer[-1] += 1
        

    return answer