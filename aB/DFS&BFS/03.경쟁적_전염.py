from collections import deque

n, k = map(int, input().split())

board = []
virus_list = []
q = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for r in range(n):
    board.append(list(map(int, input().split())))

    for c in range(n):
        if board[r][c] != 0:
            virus_list.append((board[r][c], 0, r, c))

virus_list.sort()
q = deque(virus_list)


ts, tx, ty = map(int, input().split())

while q:
    virus, s, x, y = q.popleft()

    if s == ts:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(board[tx - 1][ty - 1])
