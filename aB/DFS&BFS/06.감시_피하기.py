from itertools import combinations
import copy

n = int(input())
hall = []
students = []
teachers = []
empty_space = []

dx = [0, 1, 0 , -1]
dy = [1, 0 , -1, 0]


def dfs(copyed_hall, r, c, i):
    if r >= n or r < 0 or c >= n or c < 0 or copyed_hall[r][c] == 'O':
        return
    else:
        copyed_hall[r][c] = 'T'
        dfs(copyed_hall, r + dx[i], c + dy[i], i)

def check():
    copyed_hall = copy.deepcopy(hall)
    for r, c in teachers:
        for i in range(4):
            dfs(copyed_hall, r, c, i)
    
    for r, c in students:
        if copyed_hall[r][c] != 'S':
            return False
        
    return True

for i in range(n):
    hall_info = input().split()
    hall.append(hall_info)

for r in range(n):
    for c in range(n):
        if hall[r][c] == 'T':
            teachers.append((r, c))
        elif hall[r][c] == 'S':
            students.append((r, c))
        else:
            empty_space.append((r, c))

for candidates in list(combinations(empty_space, 3)):
    for r, c in candidates:
        hall[r][c] = 'O' # 벽설치
    if check():
        print('YES')
        break
    for r, c in candidates:
        hall[r][c] = 'X' # 다시 원래대로
else:
    print('NO')
