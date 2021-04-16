n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(n, stages):
    answer = []
    length = len(stages)

    for i in range(1, n + 1):
        count = stages.count(i)

        if len(stages) == 0:
            fail = 0
        else:
            fail = count / len(stages)

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda x: x[1], reverse=True)

    answer = [i[0] for i in answer]

    return answer


print(solution(n, stages))
