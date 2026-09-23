def solution(numbers, target):
    # 노드는 number, 간선은 덧셈 혹은 뺄셈
    # 시간 복잡도는 2^20 ~ 10^6
    answer = 0
    
    # dfs 안에 인덱스, 합
    def dfs(i, cur_sum):
        nonlocal answer
        if i == len(numbers):
            answer += 1 if cur_sum == target else 0
        else:
            dfs(i + 1, cur_sum + numbers[i])
            dfs(i + 1, cur_sum - numbers[i])
        
    dfs(0, 0)
    
    return answer