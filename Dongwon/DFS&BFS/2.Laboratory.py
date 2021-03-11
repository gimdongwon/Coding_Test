# 1. 벽을 세우기
# 2. 바이러스 최대한으로 퍼뜨려서 안전한 구역 찾기

import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    global answer
    w = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if w[i][j] == 2:
                queue.append([i,j])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 안되는 경우 찾지 말고 되는 경우로 바로 접근
            # 기존과는 다른 풀이
            if -1 < nx < n and -1 < ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    queue.append([nx,ny])
    cnt = 0
    for i in w:
        cnt += i.count(0)
    answer = max(answer, cnt)

# 벽 세우기 브루트 포스 방식
def wall(a):
    if a == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(a+1)
                # 원래의 graph로 변경
                graph[i][j] = 0
    
wall(0)
print(answer)