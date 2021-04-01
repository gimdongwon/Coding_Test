def check(answer):
    for x, y, structure in answer:
        # 기둥
        if structure == 0:
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        # 보
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
        
    return True
            
            

def solution(n, build_frame):
    answer = []
    
    for x, y, structure, action in build_frame:
        # 설치
        if action == 1:
            answer.append([x, y, structure])
            if not check(answer):
                answer.remove([x, y, structure])
                
        # 삭제
        else:
            answer.remove([x, y, structure])
            if not check(answer):
                answer.append([x, y, structure])
    
    return sorted(answer)
    