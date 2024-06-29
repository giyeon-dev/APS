from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    priorities = list(map(int, input().split()))
    deq = deque([(idx, priority) for idx, priority in enumerate(priorities)])

    order = 0
    while deq:
        q = deq.popleft()
        has_priority = False
        for i, p in deq:
            if q[1] < p:
                has_priority = True
                break
        
        # 더 큰 우선 순위가 있으면 deq 뒤로, 아니면 출력/ 타겟 M번째 순서 체크
        if has_priority:
            deq.append(q)
        else:
            order += 1
            if q[0] == M:
                print(order)
                break
