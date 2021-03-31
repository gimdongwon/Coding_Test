from collections import deque

N = 10  # 보드 크기
K = 4  # 사과 개수
apples = [(1, 2), (1, 3), (1, 4), (1, 5)]  # (y축, x축)
direct_changes = [(8, "D"), (10, "D"), (11, "D"), (13, "L")]  # 움직임


def turn_key(direct, direction):
    if direct == "D":
        next_key = direction.popleft()
        direction.append(next_key)
    elif direct == "L":
        next_key = direction.pop()
        direction.leftappend(next_key)


def solution(N, K, apples, direct_changes):
    count = 0
    board = [[0] * N for __ in range(N)]
    direction = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
    current_position = [0, 0]
    board[0][0] = 1
    snake_body = deque([(0, 0)])

    for apple in apples:
        y, x = apple
        board[y - 1][x - 1] = float("inf")

    print(board)

    for direct in direct_changes:
        seconds, direct_key = direct

        for _ in range(seconds):
            count += 1
            y, x = current_position
            px, py = direction[0]
            dx = px + x
            dy = py + y

            if dx < 0 or dx > (N - 1) or dy < 0 or dy > (N - 1) or board[dy][dx] == 1:
                return count
            elif board[dy][dx] == float("inf"):
                board[dy][dx] = 1
                snake_body.append((dy, dx))
                current_position = [dy, dx]
            else:
                board[dy][dx] = 1
                ry, rx = snake_body.popleft()
                board[ry][rx] = 0
                current_position = [dy, dx]
                snake_body.append((dy, dx))
        turn_key(direct_key, direction)

    return count


print(solution(N, K, apples, direct_changes))