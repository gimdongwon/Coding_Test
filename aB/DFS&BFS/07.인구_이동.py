from collections import deque

n, l, r = map(int, input().split())
country = []
answer = 0

dx = [0, 1, 0 , -1]
dy = [1, 0 , -1, 0]

for _ in range(n):
    country.append(list(map(int, input().split())))

def bfs(x, y, union_index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = union_index
    acc = country[x][y] # 현재 연합 인구수 누적 값
    count_country = 1 # 연합 국가의 수

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인접한 국가가 아직 연합에 들어있지 않으면
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(country[nx][ny] - country[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = union_index
                    count_country += 1
                    acc += country[nx][ny]
                    united.append((nx, ny))

    for x, y in united:
        country[x][y] = acc // count_country

while True:
    union = [[-1] * n for _ in range(n)]
    union_index = 0

    for x in range(n):
        for y in range(n):
            if union[i][j] == -1:
                bfs(x, y, union_index)
                union_index += 1

    if union_index == n * n:
        break
    
    answer += 1

print(answer)

