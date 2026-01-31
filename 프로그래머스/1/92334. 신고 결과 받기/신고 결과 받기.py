def solution(id_list, report, k):
    n = len(id_list)
    answer = [0 for _ in range(n)]
    sus_id_list = []
    
    # 데이터 입력: 각 행은 사용자별 신고 받은 경우. 나를 신고한 사용자 1 아님 0
    inter = [[0 for _ in range(n)] for _ in range(n)]
    
    for list in report:
        send, receive = list.split()
        num_s = id_list.index(send)
        num_r = id_list.index(receive)
        inter[num_r][num_s] = 1
    
    # 정지 이용자 계산
    for i in range(n):
        if sum(inter[i]) >= k:
            sus_id_list.append(i)
    
    # 처리 이메일 발송
    for j in sus_id_list:
        for k in range(n):
            if inter[j][k] == 1:
                answer[k] += 1
    
    return answer