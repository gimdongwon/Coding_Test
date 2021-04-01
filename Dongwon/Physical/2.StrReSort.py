import re

def solution(N):
    # N = input()
    a = re.sub('[0-9]', "", N)
    b = re.sub('[^0-9]', "",N)
    b = sum(map(int,list(b)))
    temp = list(a)
    temp.sort()
    a = "".join(temp)
    print(a+str(b))

solution("K1KA5CB7")
solution("AJKDLSI412K4JSJ9D")