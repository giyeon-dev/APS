def solution(s):
    ans = 0
    
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    if not stack:
        ans = 1
        
    return ans