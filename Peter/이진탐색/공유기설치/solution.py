n = 3
house_list = [1, 2, 8, 4, 9]


def solution(n, house_list):
    house_list.sort()

    start = house_list[1] - house_list[0]
    end = house_list[-1] - house_list[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        value = house_list[0]
        count = 1

        for i in range(1, len(house_list)):
            if house_list[i] >= value + mid:
                value = house_list[i]
                count += 1

        if count >= n:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result


print(solution(n, house_list))
