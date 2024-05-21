def solution(babbling):
    cnt = 0
    words = ['aya', 'ye', 'woo', 'ma']
    
    
    for bab in babbling:
        for word in words:
            if (word*2) not in bab:  # 같은 발음 연속 체크
                bab = bab.replace(word, ' ')
    
        bab_lst = bab.split()
        if len(bab_lst) == 0:
            cnt += 1

        
    return cnt