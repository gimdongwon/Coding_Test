def solution(stones, k):
    result = 0
    left, right  = 0, 200000000
    while left <= right:
        mid = (left+right) // 2
        if check(stones, k, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result + 1
    
def check(temp, k, mid):
    disapper_stone = 0
    for item in temp:
        if item-mid <= 0:
            disapper_stone += 1
            if disapper_stone == k:
                return False
        else:
            disapper_stone = 0
    return True