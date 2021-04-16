# pypy3로 하면 통과
import copy
from collections import deque

n, m = map(int, input().split())
lab = []
q = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0

for _ in range(n):
    data = list(map(int, input().split()))
    lab.append(data)

# 바이러스 퍼트리기
def bfs():
    global answer

    copyed_map = copy.deepcopy(lab)
    for r in range(n):
        for c in range(m):
            if copyed_map[r][c] == 2:
                q.append((r, c))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if copyed_map[nx][ny] == 0:
                    copyed_map[nx][ny] = 2
                    q.append((nx, ny))
    
    count = 0
    for val in copyed_map:
        count += val.count(0)
    answer = max(answer, count)
  

def install_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for r in range(n):
        for c in range(m):
            if lab[r][c] == 0:
                lab[r][c] = 1
                install_wall(cnt + 1)
                lab[r][c] = 0

install_wall(0)
print(answer)
