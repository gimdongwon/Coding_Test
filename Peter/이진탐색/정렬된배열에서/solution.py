from bisect import bisect_left, bisect_right

ex_list = [1, 1, 2, 2, 2, 2, 3]
n = 2


def solution(ex_list, n):
    right = bisect_right(ex_list, n)
    left = bisect_left(ex_list, n)
    return right - left


print(solution(ex_list, n))