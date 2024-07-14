def solution(phone_book):
    prefix = {}
    
    for p in phone_book:
        prefix[p] = True
        
    for p in phone_book:
        temp = ""
        for num in p:
            temp += num
            
            if temp in prefix and temp != p:
                return False
            
    return True
    