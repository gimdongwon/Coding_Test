n = 5  # 가로세로

build_frame = [
    [1, 0, 0, 1],
    [1, 1, 1, 1],
    [2, 1, 0, 1],
    [2, 2, 1, 1],
    [5, 0, 0, 1],
    [5, 1, 0, 1],
    [4, 2, 1, 1],
    [3, 2, 1, 1],
]  # x, y, 구조물 종류(0기둥 1보), 삭제여부(0삭제 1설치)


def check_install_column(board, y, x):
    if y == 0:
        return True
    elif board[y - 1][x] == 1 or board[y][x - 1] == 2 or board[y][x] == 2:
        return True
    else:
        return False


def check_install_beam(board, y, x):
    if board[y - 1][x] == 1 or board[y - 1][x + 1] == 1 or board[y][x - 1] == 2:
        return True
    else:
        return False


def check_remove_column(board, y, x):
    if board[y + 1][x] == 1:
        return False
    elif board[y][x - 1] == 2 and board[y + 1][x + 1] == 2:
        return False
    elif board[y+1][x] == 2 and 
    return


def check_remove_beam(board, y, x):
    return


def solution(n, build_frame):
    board = [[float("inf")] * n for _ in range(n)]

    for command in build_frame:
        x, y, cons, install = command
        if install == 0:
            if cons == 0:
                if check_install_column(board, y, x):
                    board[y][x] = 1
            elif cons == 1:
                if check_install_beam(board, y, x):
                    board[y][x] = 2
        if install == 1:
            if cons == 0:
                if check_remove_column(board, y, x):
                    board[y][x] = float("inf")
            elif cons == 1:
                if check_remove_beam(board, y, x):
                    board[y][x] = float("inf")

    return


print(solution(n, build_frame))
