def solution(bandage, health, attacks):
    ans = health
    in_a_row = 0    # 연속 카운트
    full_time = attacks[-1][0]  # 최종 공격시간
    current_time = 0
    num_attacks = len(attacks) # 공격 횟수
    attack_idx = 0 # 공격 인덱스
    
    
    while current_time <= full_time:

        # 공격처리
        if attack_idx < num_attacks and current_time == attacks[attack_idx][0]:
            ans -= attacks[attack_idx][1]
            in_a_row = 0
            if ans <= 0:
                return -1
            attack_idx += 1
        # 회복
        else:
            if ans < health:
                ans += bandage[1]
                if ans > health:
                    ans = health
                in_a_row += 1
                
                # 추가 회복
                if in_a_row == bandage[0]:
                    ans += bandage[2]
                    if ans > health:
                        ans = health
                    in_a_row = 0
            else:
                in_a_row = 0

            
        current_time += 1

    return ans

          
            
    


                