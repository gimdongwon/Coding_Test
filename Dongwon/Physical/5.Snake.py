from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

graph = [[0]*N for __ in range(N)]

# 사과 배치
for __ in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
L = int(input())
times = {}
for i in range(L):
    x,c = input().split()
    times[int(x)] = c

def turn(d,c):
    if c == "L":
        d = (d-1) % 4
    else:
        d = (d+1) % 4
    return d

dx,dy = [0,1,0,-1], [-1,0,1,0]
direction = 1
time = 1
x,y = 0,0
visited = deque([[x,y]])
graph[x][y] = 2

while True:
    x, y = x + dx[direction], y + dy[direction]
    if -1 < x < N and -1 < y < N and graph[x][y] != 2:
        if not graph[x][y] == 1:
            temp_x, temp_y = visited.pop()
            graph[temp_x][temp_y] = 0
        graph[x][y] = 2
        visited.append([x,y])
        if time in times.keys():
            direction = turn(direction, times[time])
        time += 1
    else:
        break
        # return time
print(time)