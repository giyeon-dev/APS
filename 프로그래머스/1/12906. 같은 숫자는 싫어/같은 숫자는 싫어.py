def solution(arr):
    stack = []
    
    # 스택이 비어있거나 스택의 최상위 원소와 다른 경우 스택에 추가
    for num in arr:
        if not stack or num != stack[-1]:
            stack.append(num)
    return stack