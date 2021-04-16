from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
distance[x] = 0
q = deque([x])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

while q:
    now = q.popleft()

    for next_city in graph[now]:
        if distance[next_city] == -1:
            distance[next_city] = distance[now] + 1
            q.append(next_city)

if k not in distance:
    print(-1)
else:
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
            