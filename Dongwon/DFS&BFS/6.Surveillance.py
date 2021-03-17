# 내가 생각한 풀이
# 선생님들의 위치를 파악해서 x축, y축을 감시한다 하고
# 방해벽을 설치할 수 있는 후보군을 선출
# 그 후 조합을 통해 가능 여부 판단.

# 블로그 풀이
# 선생님들의 위치가 아니라 장애물을 쌓을 수 있는 전체 후보군을 선출해서
# 장애물 위치를 조합으로 확인해서 선생님이 확인할 수 있는 경우가 하나라도 있으면 아웃
# 백트레킹 같음..

# 풀때는 완전 탐색으로 해결

import sys
from itertools import combinations
import copy

input = sys.stdin.readline

N = int(input())
graph = []

for __ in range(N):
    graph.append(list(input().split()))

wallCandinates = []
teachers = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == "X":
            wallCandinates.append([i,j])
        elif graph[i][j] == "T":
            teachers.append([i,j])

result = list(combinations(wallCandinates, 3))

def setWall(candi):
    for item in candi:
        copyGraph = copy.deepcopy(graph)
        for i in range(3):
            copyGraph[item[i][0]][item[i][1]] = "O"
        # 하나라도 통과한 경우
        if checkSurveillance(copyGraph, teachers) == True:
            return "YES"
    return "NO"

def checkSurveillance(graphs, teacher):
    # graphs에 주어진 경우가 장애물이 학생들을 전부 가려준 경우만 Ture 반환
    # 완전 탐색
    global N
    for item in teacher:
        x, y = item
        nx, ny = x,y
        while nx > 0:
            nx -= 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
        nx, ny = x,y
        while nx < N-1:
            nx += 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
        nx, ny = x,y
        while ny > 0:
            ny -= 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
        nx, ny = x,y
        while ny < N-1:
            ny += 1
            if graphs[nx][ny] == "S":
                return False
            elif graphs[nx][ny] == "O":
                break
    return True
    
answer = setWall(result)
print(answer)