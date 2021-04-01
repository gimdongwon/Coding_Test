import sys
from collections import deque

input = sys.stdin.readline

# call func

N = 6
K = 3
apples = [[3,4],[2,5],[5,3]]
L = 3
rotations = [['3', 'D'], ['15', 'L'], ['17', 'D']]

# N = int(input())
# K = int(input())

# apples = [list(map(int, input().split())) for __ in range(K)]

# L = int(input())

# rotations = [input().split() for __ in range(L)]

graph = [[0]*(N) for __ in range(N)]
current = [[0,0]]
second = 0
direction = "R"
dx,dy = [-1,1,0,0],[0,0,-1,1]
for item in apples:
    graph[item[0]-1][item[1]-1] = 1
q = deque([(0,0)])

while True:
    # 종료 조건 
    # 1. 벽에 부딪히거나
    # 2. 꼬리에 부딪히거나
    # 회전
    for item in rotations:
        if second == int(item[0]):
            if item[1] == "L":
                if direction == "R":
                    direction = "U"
                elif direction == "L":
                    direction = "D"
                elif direction == "U":
                    direction = "L"
                else:
                    direction = "R"
            else:
                if direction == "R":
                    direction = "D"
                elif direction == "L":
                    direction = "U"
                elif direction == "U":
                    direction = "R"
                else:
                    direction = "L"

    x,y = q.popleft()
    temp = 1
    if direction == "R":
        temp = 1
    elif direction == "L":
        temp = 0
    elif direction == "U":
        temp = 2
    elif direction == "D":
        temp = 3
    
    x += dx[temp]
    y += dy[temp]
    
    if x>=N or x<0 or y<0 or y>=N:
        break
    else:
        second += 1
        q.append([x,y])
    print(x,y)
    print(second)


        
    
    


print(graph)