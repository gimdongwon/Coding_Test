# 1차 실패 풀이

def solution(k, room_number):
    result = []
    used = [False for __ in range(k+1)]
    room_dict = dict()
    for i in range(1, k+1):
        room_dict[i] = i
    
    for item in room_number:
        # print(room_dict, item)
        # print(used,used[item], result)
        if not used[item]:
            used[item] = True
            result.append(item)
            temp = item
            while used[temp]:
                temp += 1
            room_dict[item] = temp
        else:
            temp = item
            while used[temp]:
                temp += 1
            
            result.append(room_dict[temp])
            used[room_dict[temp]] = True
            room_dict[temp] = temp
        
    return result

# 2차 풀이

def solution2(k, room_number):
    result = []
    room_dict = dict()
    
    for number in room_number:
        num = room_dict.get(number, 0)
        if num:
            temp = [number]
            while True:
                idx = num
                num = room_dict.get(num, 0)
                if not num:
                    result.append(idx)
                    room_dict[idx] = idx + 1
                    for i in temp:
                        room_dict[i] = idx + 1
                    break
                temp.append(num)
        else:
            result.append(number)
            room_dict[number] = number + 1
        
    return result