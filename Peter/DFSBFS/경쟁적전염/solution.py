from collections import deque

N = 3
K = 3
S = 1
check_position = (2, 2)  # Y축, X축   -1 해야함
board = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]


def solution(N, K, check_position, board):
    virus_position = []
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for y_index, y_number in enumerate(board):
        for x_index, x_number in enumerate(board[y_index]):
            if board[y_index][x_index] != 0:
                virus_number = board[y_index][x_index]
                virus_position.append((virus_number, y_index, x_index))

    virus_position.sort()
    virus_dequeue = deque(virus_position)
    virus_dequeue.append((float("inf"), 0, 0))

    while virus_dequeue:
        number, sy, sx = virus_dequeue.popleft()
        if number == float("inf"):
            break
        for py, px in direction:
            dx = sx + px
            dy = sy + py
            if dx < 0 or dx > (N - 1) or dy < 0 or dy > (N - 1):
                continue
            elif board[dy][dx] == 0:
                board[dy][dx] = number
                virus_dequeue.append((number, dy, dx))

    cy, cx = check_position

    return board[cy - 1][cx - 1]


print(solution(N, K, check_position, board))