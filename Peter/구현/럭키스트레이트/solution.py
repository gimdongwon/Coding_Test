n = 7755


def solution(n):
    front = []
    back = []

    for i in range(len(str(n)) // 2):
        front.append(int(str(n)[i]))
        back.append(int(str(n)[-i - 1]))

    if sum(front) == sum(back):
        print("LUCKY")
    else:
        print("READY")
    return


print(solution(n))