def solution(gems):
    n = len(set(gems))
    answer = [0, len(gems) - 1]
    start, end = 0,0
    current = {gems[0]: 1}

    while start < len(gems) and end < len(gems):
        if len(current) == n:
            if answer[1] - answer[0] > end - start:
                answer[0] = start
                answer[1] = end
            if current[gems[start]] == 1:
                del current[gems[start]]
            else:
                current[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if len(gems) == end:
                break
            else:
                if current.get(gems[end]) is None:
                    current[gems[end]] = 1
                else:
                    current[gems[end]] += 1
    answer[0] += 1
    answer[1] += 1
    print(answer)
    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])