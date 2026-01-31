def solution(today, terms, privacies):
    answer = []
    
    # *** 모든 월 28일이므로 전체 일수로 계산 ***
    
    # 약관 저장
    dict = {}
    for t in terms:
        rule, mm = t.split()
        dict[rule] = int(mm)
    
    # 날짜를 총 일수로 변환
    def into_days(date):
        y, m, d = map(int, date.split('.'))
        return y*12*28 + m*28 + d
    
    today_days = into_days(today)

    # 유효기간 비교
    for idx, p in enumerate(privacies, start=1):
        date, rule = p.split()
        expire_days = into_days(date) + dict[rule]*28 -1
        if expire_days < today_days:
            answer.append(idx)
    
    return answer