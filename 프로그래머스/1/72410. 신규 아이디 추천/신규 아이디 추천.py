def solution(new_id):
    # 1. lower()로 모두 소문자
    new_id = new_id.lower()

    # 2. 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자 제거
    answer = ''
    for char in new_id:
        if char.isalnum() or char in "-_.":
            answer += char
    
    # 3. 마침표 2번 이상이면 하나로 (4번 이상이면?)
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4. 마침표가 처음이나 끝이면 제거
    answer = answer.strip('.')
    
    # 5. 빈 문자열이면 'a' 대입
    if not answer:
        answer = "a"
        
    # 6. 길이가 16자 이상이면 첫 15개만, 끝 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
    
    # 7. 길이가 2자 이하라면, 길이가 3이 되게
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer