def check(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y==0 or [x-1, y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1, y-1, 0] in answer or ([x-1, y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for item in build_frame:
        x, y, types, status = item
        answerFormat = item[0:3]
        if status == 0:
            answer.remove(answerFormat)
            if not check(answer):
                answer.append(answerFormat)
        elif status == 1:
            answer.append(answerFormat)
            if not check(answer):
                answer.remove(answerFormat)
                
    return sorted(answer)