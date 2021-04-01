def solution(p):
    answer = ''
    
    if p == '':
        return answer
    
    bal_idx = balanced_index(p)
    u = p[:bal_idx + 1]
    v = p[bal_idx + 1:]
    
    if check_right_string(u) == True:
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
                
    
    return answer

def balanced_index(str):
    count = 0 # 왼쪽 괄호 개수
    for i in range(len(str)):
        if str[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i
    
def check_right_string(str):
    count = 0 # 왼쪽 괄호 개수
    for i in str:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True
    