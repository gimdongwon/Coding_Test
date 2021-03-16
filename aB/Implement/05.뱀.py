from collections import deque

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

coordinate = [[0] * (n + 1) for _ in range(n + 1)] # 전체 좌표

for _ in range(k):
    x, y = map(int, input().split())
    coordinate[x][y] = 1

l = int(input()) # 회전 횟수
l_info = [] # 회전 정보
for _ in range(l):
    x, c = input().split()
    l_info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction


def solution():
    x, y = 1, 1
    q = deque([(x, y)]) # 뱀의 위치 정보
    coordinate[x][y] = 9
    direction = 0
    l_index = 0
    time = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있고 현재 위치가 뱀의 위치가 아니면
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and coordinate[nx][ny] != 9:
            if coordinate[nx][ny] == 0:
                coordinate[nx][ny] = 9
                q.append((nx, ny))
                px, py = q.popleft()
                coordinate[px][py] = 0

            if coordinate[nx][ny] == 1:
                coordinate[nx][ny] = 9
                q.append((nx, ny))

        # 부딪히면 시간 증가시키고 끝
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1

        if l_index < l and time == l_info[l_index][0]:
            direction = turn(direction, l_info[l_index][1])
            l_index += 1

    return time

print(solution())
