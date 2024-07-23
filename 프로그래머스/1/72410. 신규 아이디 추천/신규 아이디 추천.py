def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for letter in new_id:
        if '0' <= letter <= '9' or 'a' <= letter <= 'z':
            continue
        if letter not in ('-', '_', '.'):
            new_id = new_id.replace(letter,'')
    
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    new_id = new_id.strip('.')
    
    # 5단계
    if not new_id:
        new_id = 'a'
        
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    
    # 7단계
    while len(new_id) < 3:
        new_id += (new_id[-1]) 
    
    return new_id