def solution(food):
    ans = ''
    
    player1 = player2 = ''
    for i in range(1, len(food)):
        player1 += str(i) * (food[i] // 2)
    
    player2 = player1[::-1]
    
    ans = player1 + '0' + player2
                
            
    return ans