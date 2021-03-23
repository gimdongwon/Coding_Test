N = int(input())

houses = list(map(int, input().split()))

home, result = float('inf'), float('inf')

for house in houses:
    print(house)
    sumNum = 0
    for item in houses:
        sumNum += abs(house - item)
    if home != min(home, sumNum):
        home = min(home, sumNum)
        result = house
print(result)