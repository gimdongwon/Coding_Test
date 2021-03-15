import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

second, x, y = map(int, input().split())

queue = []

currentTime = 0

items = [i for i in range(1, n+1)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                queue.append([graph[i][j],i,j, 0])

queue.sort()
queue = deque(queue)

while queue:
    print(graph, queue)
    z,a,b, time = queue.popleft()
    if time == second:
        break
    targetVirus = graph[a][b]
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if -1 < nx < n and -1 < ny < n:
            # targetVirus가 새로 추가된 virus보다 우선순위가 낮거나 0이면
            if graph[nx][ny] == 0:
                graph[nx][ny] = targetVirus
                queue.append([graph[nx][ny], nx, ny, currentTime+1])
print(graph[x-1][y-1])