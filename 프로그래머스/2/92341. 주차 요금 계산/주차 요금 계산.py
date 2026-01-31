import math
from collections import defaultdict

def solution(fees, records):
    base_time, base_fee, time_gap, fee_gap = fees
    answer = []
    
    def minutes(str):  # HH:MM
        hh = int(str[0:2])
        mm = int(str[3:5])
        return hh*60+mm
    
    # *****
    in_time = {}
    total_time = defaultdict(int)
    # *****
    
    for record in records:
        time, car, status = record.split(' ')
        time = minutes(time)
        
        if status == 'IN':
            in_time[car] = time
        else: # 'OUT'
            total_time[car] += time - in_time[car]
            del in_time[car]
        
    # 출차 안한 차 23:59 처리
    for car, time in in_time.items():
        total_time[car] += minutes("23:59") - time
    
    # total_time에서 요금 계산
    for car, time in sorted(total_time.items()):
        cost = 0
        if time <= base_time:
            cost = base_fee
        else:
            extra_time = time - base_time
            cost = base_fee + math.ceil(extra_time/time_gap) * fee_gap
        answer.append(cost)
    
    return answer
