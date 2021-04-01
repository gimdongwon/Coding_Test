# dfs로 연산자 순서를 따로 정하지 않고 백트레킹으로 전체를 탐색.

import sys

input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
operater = list(map(int, input().split()))

minimum = float("inf")
maximum = float("-inf")

def dfs(now, level):
    if level == N:
        global maximum, minimum
        print(maximum, minimum)
        maximum = max(now, maximum)
        minimum = min(now, minimum)
        return
    if operater[0] > 0:
        operater[0] -= 1
        dfs(now + numList[level], level + 1)
        operater[0] += 1
    if operater[1] > 0:
        operater[1] -= 1
        dfs(now - numList[level], level + 1)
        operater[1] += 1
    if operater[2] > 0:
        operater[2] -= 1
        dfs(now * numList[level], level + 1)
        operater[2] += 1
    if operater[3] > 0:
        result = abs(now)//numList[level]
        if now < 0:
            result *= -1
        operater[3] -= 1
        dfs(result, level+1)
        operater[3] += 1

now = numList[0]
dfs(now, 1)

print(maximum)
print(minimum)