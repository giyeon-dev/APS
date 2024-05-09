def solution(arr):
    answer = 0
    sum = 0
    cnt = len(arr)
    
    for i in range(cnt):
        sum += arr[i]
    
    answer = sum / cnt
    return answer