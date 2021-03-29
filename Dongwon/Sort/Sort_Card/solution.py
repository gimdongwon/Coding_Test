import heapq
import sys 

input = sys.stdin.readline

N = int(input())
Cards = []

for __ in range(N):
    Cards.append(int(input()))

result = 0
heapq.heapify(Cards)

while len(Cards) > 1:
    x = heapq.heappop(Cards)
    y = heapq.heappop(Cards)
    heapq.heappush(Cards, x+y)
    result += x+y

print(result)