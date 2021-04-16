fixN = N = int(input())
result = 0

while True:
    a,b = N // 10, N % 10
    res = a + b
    result += 1
    N = int(str(N%10) + str(res%10))
    if fixN == N:
        break
    
print(result)
