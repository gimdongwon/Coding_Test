from collections import deque
from math import inf

def solution(board):
    
    def bfs(start):
        table = [[inf for __ in range(len(board))] for __ in range(len(board))]
        # up, left, down, right
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        queue = deque([start])
        table[0][0] = 0
        while queue:
            x, y, cost, head = queue.popleft()
            for idx, (dx, dy) in enumerate(dirs):
                nx,ny = x+dx, y+dy
                n_cost = cost + (600 if idx != head else 100)
                if -1 < nx < len(board) and -1 < ny < len(board) and board[nx][ny] == 0 and table[nx][ny] > n_cost:
                    table[nx][ny] = n_cost
                    queue.append([nx,ny,n_cost, idx])
        print(table)
        # 도착은 고정
        return table[-1][-1]
    # 출발은 아래 혹은 오른쪽이므로
    
    return min(bfs((0,0,0,2)), bfs((0,0,0,3)))