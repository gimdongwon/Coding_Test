word = "AJKDLSI412K4JSJ9D"


def solution(word):
    number_arr = str(sum([int(i) for i in word if i.isdigit()]))
    word_arr = [i for i in word if not i.isdigit()]
    word_arr.sort()
    word_arr.append(number_arr)
    answer = "".join(word_arr)

    return answer


print(solution(word))