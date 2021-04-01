import itertools
N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

home = []
chickenHome = []
distance = 0
distanceZip = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i,j])
        elif arr[i][j] == 2:
            chickenHome.append([i,j])
result = chickenHome

if M != 1:
    result = list(itertools.combinations(chickenHome, M))
    for resultItem in result:
        distance = 0
        for homeItem in home:
            temp = []
            for resultItem2 in resultItem:
                temp.append(abs(resultItem2[0]-homeItem[0]) + abs(resultItem2[1]-homeItem[1]))
            distance += min(temp)
        distanceZip.append(distance)
else:
    for resultItem in result:
        distance = 0
        for homeItem in home:
            distance += abs(resultItem[0] - homeItem[0]) + abs(resultItem[1] - homeItem[1])
        distanceZip.append(distance)

print(min(distanceZip))