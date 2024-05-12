def solution(array, commands):
    answer = []
    i = j = k = 0
    num = 0
    new_arr = []
    for m in range(len(commands)):
        i = commands[m][0]
        j = commands[m][1]
        k = commands[m][2]
    
        new_arr = sorted(array[i-1:j])
        num = new_arr[k-1]
        answer.append(num)
        
    return answer