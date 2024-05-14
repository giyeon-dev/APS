# 이진수 변환 - stack 활용
def binary(num, n):
    stack = []
    while num > 0:
        remain = num % 2
        stack.append(str(remain))
        num = num // 2

    bi_num = ''
    while stack:
        bi_num += stack.pop()

    return '0' * (n - len(bi_num)) + bi_num

def solution(n, arr1, arr2):
    answer = []
   
    for i in range(n):
        row = ''
        bin1 = binary(arr1[i], n)
        bin2 = binary(arr2[i], n)
        for j in range(n):
            if bin1[j] == '1' or bin2[j] == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)
    return answer
                
    return answer