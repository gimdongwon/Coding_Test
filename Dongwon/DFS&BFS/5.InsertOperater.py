import copy
import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

# 1.덧셈 2.뺄셈 3.곱셈 4.나눗셈
Operater = list(map(int, input().split()))
Operater2 = copy.deepcopy(Operater)
answer = 0
answer2 = 0

def maxNum(answer):
    # 1.뺄셈 2.나눗셈 3.덧셈 4.곱셈
    for i in range(len(A)):
        if i == 0:
            answer += A[i]
        else:
            if Operater[1] > 0:
                answer -= A[i]
                Operater[1] -= 1
            else:
                if Operater[3] > 0:
                    answer = int(answer / A[i])
                    Operater[3] -= 1
                else:
                    if Operater[0] > 0:
                        answer += A[i]
                        Operater[0] -= 1
                    elif Operater[2] > 0:
                        answer *= A[i]
                        Operater[2] -= 1
    return answer
def minNum(answer):
    # 다 잇을때 : 1.덧셈 2.나눗셈 3.뺄셈 4.곱셈
    # 뺄셈없을때 : 1.나눗셈 2.곱셈 3.덧셈
    if Operater2[1] == 0:
        for i in range(len(A)):
            if i ==0:
                answer += A[i]
            else:
                if Operater2[3] > 0:
                    answer = int(answer / A[i])
                    Operater2[3] -= 1
                else:
                    if Operater2[2] > 0:
                        answer *= A[i]
                        Operater2[2] -= 1
                    elif Operater2[0] > 0:
                        answer += A[i]
                        Operater2[0] -= 1
    else:
        for i in range(len(A)):
            if i == 0:
                answer += A[i]
            else:
                if Operater2[0] > 0:
                    answer += A[i]
                    Operater2[0] -= 1
                else:
                    if Operater2[3] > 0:
                        answer = int(answer / A[i])
                        Operater2[3] -= 1
                    else:
                        if Operater2[1] > 0:
                            answer -= A[i]
                            Operater2[1] -= 1
                        elif Operater2[2] > 0:
                            answer *= A[i]
                            Operater2[2] -= 1
    return answer

print(maxNum(answer))
print(minNum(answer2))