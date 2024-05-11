def solution(s, n):
    
    # 아스키 코드 활용
    new_char =''
    for char in s:
        if char.islower() and ord(char) + n > 122:
            new_char += chr(ord(char) -26 + n )
           
        elif char.isupper() and ord(char) + n > 90:
            new_char += chr(ord(char) -26 + n)
            
        elif ord(char) == 32:
            new_char += " "
        else:
            new_char += chr(ord(char) + n)
        
        
    
    return ''.join(new_char)