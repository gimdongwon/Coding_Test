from collections import deque

def get_movable_pos(pos, board):
    next_pos = []
    pos = list(pos)
    
    pos_x1 = pos[0][0] 
    pos_y1 = pos[0][1]
    pos_x2 = pos[1][0]
    pos_y2 = pos[1][1]
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    for i in range(4):
        n_pos_x1 = pos_x1 + dx[i]
        n_pos_y1 = pos_y1 + dy[i]
        n_pos_x2 = pos_x2 + dx[i]
        n_pos_y2 = pos_y2 + dy[i]
        
        if board[n_pos_x1][n_pos_y1] == 0 and board[n_pos_x2][n_pos_y2] == 0:
            next_pos.append({(n_pos_x1, n_pos_y1), (n_pos_x2, n_pos_y2)})
    
    if pos_x1 == pos_x2:
        for i in [1, -1]:
            if board[pos_x1 + i][pos_y1] == 0 and board[pos_x2 + i][pos_y2] == 0:
                next_pos.append({(pos_x1, pos_y1), (pos_x1 + i, pos_y1)})
                next_pos.append({(pos_x2, pos_y2), (pos_x2 + i, pos_y2)})
    else:
        for i in [1, -1]:
            if board[pos_x1][pos_y1 + i] == 0 and board[pos_x2][pos_y2 + i] == 0:
                next_pos.append({(pos_x1, pos_y1), (pos_x1, pos_y1 + i)})
                next_pos.append({(pos_x2, pos_y2), (pos_x2, pos_y2 + i)})
    
    return next_pos

def solution(board):
    answer = 0
    N = len(board)
    new_board = [[1] * (N + 2) for _ in range(N + 2)]
    
    q = deque()
    visited = []
    
    pos = {(1, 1), (1, 2)}
    
    q.append((pos, 0))
    visited.append(pos)
    
    for i in range(N):
        for j in range(N):
            new_board[i + 1][j + 1] = board[i][j]
    
    while q:
        pos, distance = q.popleft()
        
        if (N, N) in pos:
            return distance
        
        for next_pos in get_movable_pos(pos, new_board):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos, distance + 1))
    
    return 0