# https://www.acmicpc.net/status?user_id=ehddnjs89&problem_id=2110&from_mine=1
import sys
input = sys.stdin.readline
N, C = map(int, input().split())

houses = []
for __ in range(N):
    houses.append(int(input()))

houses.sort()

start, end, result = 1, houses[-1]-houses[0], 0
result = 0
while start <= end:
    mid = (start + end) // 2
    old = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if houses[i] >= old+mid:
            count+=1
            old = houses[i]
    
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)