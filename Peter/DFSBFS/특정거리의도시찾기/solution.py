from collections import deque

n = 4
k = 2
x = 1
info_array = [(1, 2), (1, 3), (2, 3), (2, 4)]


def solution(n, k, x):
    board = [float("inf")] * (n + 1)
    road = deque(
        [(src_vil, next_vil) for src_vil, next_vil in info_array if src_vil == x]
    )
    board[x] = 0

    if not road:
        return -1

    while road:
        src_vil, next_vil = road.popleft()
        if board[src_vil] + 1 < board[next_vil]:
            board[next_vil] = board[src_vil] + 1

        for s, n in info_array:
            if s == next_vil:
                road.append((s, n))

    answer = [i for i, j in enumerate(board) if j == k]

    if not answer:
        return -1

    return answer


print(solution(n, k, x))
