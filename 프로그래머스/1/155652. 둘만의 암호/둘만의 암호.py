def solution(s, skip, index):
    ans = ''
    skip_lst = list(skip)
    
    
    for letter in s:
        cnt = 0
        while cnt < index:
            letter = chr(ord(letter) + 1)
            
            if ord(letter) > ord('z'):
                letter = chr(ord(letter) - 26)
          
            if letter in skip_lst:
                continue
    
            cnt += 1
        
        ans += letter
    
    return ans