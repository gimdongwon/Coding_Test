# result.sort(key=len)
# len(min(result, key=len))
# min으로 하면 길이에 따른 정렬이 아니라 아스키 코드정렬이므로
# 꼭 key = len을 넣어주자

import copy

def solution(s):
    if len(s) == 1: return 1
    # 하나는 돌기만 하고 
    # 하나는 압축만 하기
    a = list(s)
    b = copy.deepcopy(a)
    result = []
    
    for i in range(1, len(s)//2+1):
        temp = []
        for j in range(0, len(b), i):
            temp.append("".join(b[j:j+i]))
        
        num = 1
        temp2 = []
        for j in range(len(temp)-1):
            if temp[j] == temp[j+1]:
                num += 1
                if j == len(temp)-2:
                    temp2.append(str(num) + temp[j])    
            else:
                if num > 1:
                    temp2.append(str(num) + temp[j])
                else:
                    temp2.append(temp[j])
                if j == len(temp)-2:
                    temp2.append(temp[j+1])
                num = 1
        result.append("".join(temp2))
    print(len(min(result)))
solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")

