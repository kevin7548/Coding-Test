def solution(record):
    answer = []
    id_nick = {}
    
    # 최종 닉네임 매핑
    for list in record:
        if list[0] in ('E', 'C'):   # Enter 또는 Change
            state, user_id, nickname = list.split()
            id_nick[user_id] = nickname
        else:    # Leave
            state, user_id = list.split()
    
    # 문자열 출력
    for list in record:
        parts = list.split()
        state, user_id = parts[0], parts[1]
        
        if state == 'Enter':
            answer.append(f"{id_nick[user_id]}님이 들어왔습니다.")
        elif state == 'Leave':
            answer.append(f"{id_nick[user_id]}님이 나갔습니다.")
        
    return answer

# 최종 닉네임 먼저 매핑하고, 그 다음 메시지 출력
# split() 결과 개수 다르면, 먼저 parts로 나누고 배정