from itertools import combinations

n, m = map(int, input().split())
chickens = []
homes = []

for r in range(n):
    coordinate = list(map(int, input().split()))
    for c in range(n):
        if coordinate[c] == 1:
            homes.append((r, c))
        if coordinate[c] == 2:
            chickens.append((r, c))

chiken_list = list(combinations(chickens, m))

def get_distance(home, chicken):
    hx, hy = home
    cx, cy = chicken
    return abs(hx - cx) + abs(hy - cy)

def get_chicken_distance(chiken_val):
    result = 0

    for home in homes:
        temp = 1e9
        for chicken in chiken_val:
            temp = min(temp, get_distance(home, chicken))
        result += temp
    return result

# 이제 치킨 거리의 합의 최소를 찾아서 출력한다.
result = 1e9
for chiken_val in chiken_list:
    result = min(result,get_chicken_distance(chiken_val))

print(result)
