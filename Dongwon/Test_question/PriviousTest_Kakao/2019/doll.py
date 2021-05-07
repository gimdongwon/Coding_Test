# 1차 풀이 list 이용해서 pop(0)으로 해결

def solution(board, moves):
    result = 0
    stack = []
    change_board = [[] for __ in range(len(board))]
    
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board)):
            if board[j][i] != 0:
                change_board[i].append(board[j][i])
    print(change_board)
    for item in moves:
        if len(change_board[item-1]) == 0:
            continue
            
        first = change_board[item-1].pop(0)
        print(first, item, stack)
        if len(stack) != 0:
            second = stack.pop()
            if first == second:
                result += 2
            else:
                stack.append(second)
                stack.append(first)
        else:
            stack.append(first)
    return result
            
        

# 2차 풀이 deque 이용.

from collections import deque

def solution2(board, moves):
    result = 0
    stack = []
    change_board = [deque([]) for __ in range(len(board))]
    
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board)):
            if board[j][i] != 0:
                change_board[i].append(board[j][i])
    # print(change_board)
    for item in moves:
        if len(change_board[item-1]) == 0:
            continue
            
        first = change_board[item-1].popleft()
        # print(first, item, stack)
        if len(stack) != 0:
            second = stack.pop()
            if first == second:
                result += 2
            else:
                stack.append(second)
                stack.append(first)
        else:
            stack.append(first)
    return result
            
        