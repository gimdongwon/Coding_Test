# class way1:
#     INF = int(1e9)
#     n, m = 6, 11
#     start = 1

#     graph = [
#                 [1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],
#                 [3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],
#                 [5,6,2]
#     ]

#     visited = [False] * (n+1)
#     distance = [INF] * (n+1)

#     def get_smalllest_node():
#         min_value = INF
#         index = 0
#         for i in range(1, n+1):
#             if distance[i] < min_value and not visited[i]:
#                 min_value = distance[i]
#                 index = 1
#         return index

#     def dijkstra(start):
#         distance[start] = 0
#         visited[start] = True

#         for j in graph[start]:
#             distance[j[0]] = j[1]
        
#         for i in range(n-1):
#             now = get_smalllest_node()
#             visited[now] = True

#             for j in graph[now]:
#                 cost = distance[now] + j[1]
#                 if cost < distance[j[0]]:
#                     distance[j[0]] = cost

#     dijkstra(start)

#     for i in range(1, n+1):
#         if distance[i] == INF:
#             print("INFINITY")
#         else:
#             print(distance[i])

import heapq

INF = int(1e9)
n,m = 6,11
start = 1

graph = [[],[(2,2), (3,5), (4,1)], [(3,3), (4,2)], [(2,3), (6,5)], [(3,3), (5,1)], [(3,1), (6,2)], []]

distance = [INF] * (n+1)

q = []
heapq.heappush(q, (0,start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])