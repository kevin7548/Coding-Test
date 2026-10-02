def solution(new_id):
    answer = ''
    # 1. lower()로 모두 소문자
    new_id = new_id.lower()

    # 2. 
    for char in new_id:
        if char.isalnum() or char in "-_.":
            answer += char 
    
    # 3. 마침표 2번 이상이면 하나로 (4번 이상이면?)
    for i in range(len(answer), 1, -1):
        answer = answer.replace('.'*i, '.')
    
    # 4.
    if answer.startswith('.'):
        answer = answer[1:]
    if answer[::-1].startswith('.'):
        answer = answer[:-1]
    
    # 5.
    if answer == "":
        answer = "a"
        
    # 6.
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[::-1].startswith('.'):
        answer = answer[:-1]
    
    # 7.
    if len(answer) == 1:
        answer = answer*3
    elif len(answer) == 2:
        answer += answer[-1]
    
    return answer