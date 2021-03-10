class practice:
    graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    

    visited = [False]*len(graph)
    # dfs(graph, 1, visited)
    from collections import deque

    def bfs(graph, v, visited):
        queue = deque([v])
        visited[v] = True
        
        while queue:
            p = queue.popleft()
            print(p, end=' ')
            for i in graph[p]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # bfs(graph, 1, visited)

class coke:   
    def beverage(icePack):
        answer = 0
        m,n = len(icePack), len(icePack[0])

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def dfs(x,y):
            if x<=-1 or x>=m or y<=-1 or y>=n:
                return False
            if icePack[x][y] == 0:
                icePack[x][y] = 1
                for i in range(4):
                    dfs(x+dx[i], y+dy[i])
                return True
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j)==True:
                    answer+=1
        # print(answer)

    # icePack = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
    icePack = [[0,0,1],[0,1,0],[1,0,1]]
    beverage(icePack)

from collections import deque

# maps = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
maps = [[1,1,0],[0,1,0],[0,1,1]]

m,n = len(maps), len(maps[0])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    return maps[m-1][n-1]

print(bfs(0,0))