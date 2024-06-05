def solution(n):
    ans = n + 1
    bin_n = bin(n)[2:]
    
    def bin_cnt(bin_n):
        cnt = 0
        for i in bin_n:
            if i == '1':
                cnt += 1
        return cnt
    
    while True:
        bin_ans = bin(ans)[2:]
        if bin_cnt(bin_n) == bin_cnt(bin_ans):
            return ans
        ans += 1
   
    return ans