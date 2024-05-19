def solution(s):
    result = []
    while s:
        x = s[0]
        cnt_x = 1
        cnt_other = 0
        for char in s[1:]:
            if char == x:
                cnt_x += 1
            else:
                cnt_other += 1
            if cnt_x == cnt_other:
                result.append(s[:cnt_x + cnt_other])
                s = s[cnt_x + cnt_other:]
                break
        else:
            result.append(s)
            break
    return len(result)