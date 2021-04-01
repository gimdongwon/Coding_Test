from itertools import product
from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

operations = list(product(['+', '-', '*', '/'], repeat=(n - 1)))
possible_operations = []

for oper in operations:
    if oper.count('+') == add and oper.count('-') == sub and oper.count('*') == mul and oper.count('/') == div:
        possible_operations.append(list(oper))

min_val = 1e9
max_val = -1e9

while possible_operations:
    opers = deque(possible_operations.pop())
    result = numbers[0]

    for i in range(1, len(numbers)):
        oper = opers.popleft()
        
        if oper == '+':
            result += numbers[i]
            
        if oper == '-':
            result -= numbers[i]

        if oper == '*':
            result *= numbers[i]

        if oper == '/':
            result = int(result / numbers[i])

    min_val = min(min_val, result)
    max_val = max(max_val, result)

print(max_val)
print(min_val)