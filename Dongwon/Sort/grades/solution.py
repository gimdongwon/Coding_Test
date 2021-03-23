import sys

input = sys.stdin.readline

N = int(input())
arr = []
for __ in range(N):
    # arr.append(input().split(" "))
    [name, kor, math, eng] = map(str, input().split(" "))
    arr.append([name, int(kor), int(math), int(eng)])

arr = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for item in arr:
    print(item[0])