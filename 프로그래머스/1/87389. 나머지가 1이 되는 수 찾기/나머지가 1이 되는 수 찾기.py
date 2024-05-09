def solution(n):

    for ans in range(1, n + 1):
        if n % ans == 1:
            return ans
        else:
            ans += 1
   