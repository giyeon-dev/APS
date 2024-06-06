def solution(brown, yellow):
    
    carpet = brown + yellow
    
    # 카펫의 최소 크기 3x3, w >= h
    for h in range(3, carpet//2 + 1):
        if carpet % h == 0:
            w = carpet // h
            if w >= h:
                if (w - 2) * (h - 2) == yellow:
                    return [w, h]
    