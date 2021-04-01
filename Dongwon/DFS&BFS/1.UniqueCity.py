from collections import deque
import sys

input = sys.stdin.readline

a,b,c,d = map(int, input().split())
graph = [[] for __ in range(a+1)]

for __ in range(b):
    x,y = map(int, input().split())
    graph[x].append(y)

distance = [-1]*(a+1)
distance[d] = 0

queue = deque([d])
while queue:
    p = queue.popleft()
    for node in graph[p]:
        if distance[node] == -1:
            distance[node] = distance[p] + 1
            queue.append(node)

check = False
for i in range(len(distance)):
    if distance[i]==c:
        print(i)
        check = True
if check == False:
    print(-1)