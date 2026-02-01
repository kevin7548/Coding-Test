def solution(files):
    answer = []
    
    # head, number 구분
    # ***
    for idx, f in enumerate(files):
        # ***
        i = 0
        # ***
        n = len(f)
        
        while i < n and not f[i].isdigit():             
            i += 1
        head = f[:i]
        
        a = i
        while i < n and f[i].isdigit():
            i += 1
        number = f[a:i]
        tail = f[i:]
        
        answer.append((head.lower(), int(number), idx, f))
    
        answer.sort(key=lambda x: (x[0], x[1], x[2]))
               
    return [x[3] for x in answer]


# abc,12, ,.,-