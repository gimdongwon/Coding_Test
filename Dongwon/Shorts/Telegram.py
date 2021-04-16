import heapq

INF = int(1e9)

n,m,start = 3,2,1
graph = [[], [(2,4), (3,2)], [],[]]
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

count = 0
max_distance = 0
print(distance)

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
print(count - 1, max_distance)