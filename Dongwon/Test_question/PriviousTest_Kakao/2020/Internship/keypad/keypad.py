def solution(numbers, hand):
    answer = ''
    position = [[3,1], [0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    left, right = [3,0], [3,2]
    for number in numbers:
        if number in [1,4,7]:
            answer += "L"
            left = position[number]
        elif number in [3,6,9]:
            answer += "R"
            right = position[number]
        else:
            left_distance = abs(left[0] - position[number][0]) + abs(left[1] - position[number][1])
            right_distance = abs(right[0] - position[number][0]) + abs(right[1] - position[number][1])
            # print(left_distance,right_distance)
            if left_distance > right_distance:
                answer += "R"
                right = position[number]
            elif left_distance < right_distance:
                answer += "L"
                left = position[number]
            else:
                if hand == "right":
                    answer += "R"
                    right = position[number]
                else:
                    answer += "L"
                    left = position[number]
    return answer