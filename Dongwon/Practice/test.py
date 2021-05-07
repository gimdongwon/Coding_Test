graph = [[], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')
    for item in graph[start]:
        if visited[item] == False:
            visited[item] = True
            dfs(item, visited)

visited = [False for __ in range(len(graph))]
# dfs(1, visited)

from collections import deque

def bfs(start, visited):
    visited[start] = True
    que = deque([start])
    while que:
        temp = que.popleft()
        print(temp, end=' ')
        for item in graph[temp]:
            if visited[item] == False:
                que.append(item)
                visited[item] = True

    

# bfs(1, visited)

ice_box = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

def beverage(ice_box):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def ice_time(x,y):
        if -1< x < len(ice_box) and -1 < y < len(ice_box[0]) and ice_box[x][y] == 0:
            ice_box[x][y] = 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                ice_time(nx,ny)
            return True
        return False
    
    result = 0
    
    for i in range(len(ice_box)):
        for j in range(len(ice_box[i])):
            if ice_time(i,j) == True:
                result += 1
                print(ice_box)
    print(result)

    # print(visited)
    # print(ice_box)

# beverage(ice_box)

def escape():
    graph = [[1,0,1,0,1,0], [1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
    # graph = [[1,1,0],[0,1,0],[0,1,1]]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < len(graph) and -1 < ny < len(graph[0]) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                # print(nx,ny)
            
    print(graph)
    # print(graph[len(graph[0])-1][len(graph)-1])
escape()