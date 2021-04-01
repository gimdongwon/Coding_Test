# 첫번째 풀이

import math

def solution(N, stages):
    result = {}
    challenger = len(stages)
    stages.sort()
    
    for i in range(1, N+1):
        if len(stages) == 0:
            result[i] = 0
            continue
        fail_num = len(list(filter(lambda x: x == i, stages)))
        result[i] = math.floor(fail_num / len(stages) * 100)
        stages = list(filter(lambda x: x!=i, stages))
    
    answer =  sorted(result.items(), key=(lambda x: x[1]), reverse=True)
    
    # return list(map(lambda x: x[0], answer))
    a = []
    for item in answer:
        a.append(item[0])
    return a

# 두번째 풀이

def solution2(N, stages):
    board = {}
    current_user = 0 # 이게 포인트
    
    for i in range(N):
        if stages.count(i+1) == 0:
            board[i+1] = 0
        else:
            board[i+1] = stages.count(i+1) / (len(stages) - current_user)
        current_user += stages.count(i+1)
    
    result = sorted(board.items(), key= lambda x: x[1], reverse=True)
    
    return [item[0] for item in result]