from heapq import heappush, heappop

def solution(N, road, K):
    
    distance = [float('inf')]*(N+1)
    distance[1] = 0
    
    # graph = [[] for _ in range(N+1)]
    # for x,y,z in road:
    #     graph[x].append((y,z))
    # print(graph)
    # q = []
    # start = 1
    # heappush(q, (0, start))
    # distance[start] = 0
    # while q:
    #     dist, now = heappop(q)
    #     if distance[now] < dist:
    #         continue
    #     for i in graph[now]:
    #         cost = dist + i[1]
    #         if cost < distance[i[0]]:
    #             distance[i[0]] = cost
    #             heappush(q, (cost, i[0]))
    # print(distance)
    heap = []
    heappush(heap, [1,0])
    while heap:
        current, current_cost = heappop(heap)
        for start, end, cost in road:
            next_cost = current_cost + cost
            # print(start, end, cost, current, distance, next_cost)
            if start == current and next_cost < distance[end]:
                distance[end] = next_cost
                heappush(heap, [end, next_cost])
            elif end == current and next_cost < distance[start]:
                distance[start] = next_cost
                heappush(heap, [start, next_cost])
    print(distance)
    return len([item for item in distance if item <= K])