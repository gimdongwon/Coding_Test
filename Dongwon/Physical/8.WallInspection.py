from itertools import permutations

def solution(n, weak, dist):
    # 친구들이 주기적으로 취약지점 점검
    # 점검시간 1시간
    # 최소한의 친구들을 투입
    leng = len(weak)
    # 원형이라 2배로 늘리고 점 갯수로 확인
    for i in range(leng):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    
    for start in range(leng):
        for friends in list(permutations(dist, len(dist))):
            # 어떤 친구를 어떤 조합으로 넣을건지 결정하기 위해 경우의 수 구함.
            count = 1
            position = weak[start]+friends[count-1]
            # print(start, friends, count, position, weak)
            
            # 전체 점을 다 지나는 지 확인하고 최솟값 정하기(여기가 핵심)
            for idx in range(start, start+leng):
                if position < weak[idx]:
                    count+=1
                    if count > len(dist):
                        break
                    position = weak[idx]+friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer