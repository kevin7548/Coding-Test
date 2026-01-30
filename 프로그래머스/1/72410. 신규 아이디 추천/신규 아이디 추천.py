def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # *** 2단계 ***
    allowed = set('abcdefghijklmnopqrstuvwxyz0123456789-_.')
    new_id = ''.join(c for c in new_id if c in allowed)
    
    # *** 3단계 ***
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # * 4단계 *
    new_id = new_id.strip('.')
    
    # 5단계
    if not new_id:
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
    return new_id