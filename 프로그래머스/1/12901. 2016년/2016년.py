def solution(a, b):
    
    # 각 월의 일 수
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 요일
    day_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    # 1월 1일 이후 총 일 수
    total_days = sum(month_days[:a-1]) + b - 1
    
    idx = total_days % 7
    
    ans = day_of_week[idx]
    
    return ans