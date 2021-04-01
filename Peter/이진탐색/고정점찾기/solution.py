ex_list = [-15, -6, 1, 3, 7]


def solution(ex_list):
    def bin_search(ex_list, start, end):
        if start > end:
            return None
        mid = (start + end) // 2

        if ex_list[mid] == mid:
            return mid
        elif ex_list[mid] > mid:
            return bin_search(ex_list, start, mid - 1)
        else:
            return bin_search(ex_list, mid - 1, end)

    index = bin_search(ex_list, 0, len(ex_list) - 1)

    return index


print(solution(ex_list))