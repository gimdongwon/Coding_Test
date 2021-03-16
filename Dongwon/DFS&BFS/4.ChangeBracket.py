# 문자 나누기
def divide(w):
    num = 0
    for i in range(len(w)):
        if w[i] == "(":
            num += 1
        else:
            num -= 1
        if num == 0:
            return w[:i+1], w[i+1:]
# 올바른 문자열 확인
def isBalance(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if not p:
        return ""
    u,v = divide(p)
    
    if isBalance(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1:-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        return answer