import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

second, x, y = map(int, input().split())