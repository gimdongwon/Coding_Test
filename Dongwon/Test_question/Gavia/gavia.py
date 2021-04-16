import math

def solution(n):
    zero = 0
    i = 1
    while n > i:
        i *= 5
        zero += math.floor(n / i)
        
    return zero

#2

import copy

def solution(s):
    good_strs = []
    check = set(s)
    
    
    for i in range(1, len(s)+1):
        for j in range(len(s)):
            if j+i > len(s):
                break
            if s[j:j+i] not in good_strs:
                good_strs.append(s[j:j+i])
    
    temp = copy.deepcopy(good_strs)
    
    for i in range(len(good_strs)):
        for item in check:
            if good_strs[i].count(item) > 1:
                if good_strs[i] in temp:
                    temp.remove(good_strs[i])
                    print(good_strs[i], item)
                
    return len(temp)

# 3
import heapq

def solution(N, coffee_times):
    result = []
    time = 0
    coffee_making = {}
    for idx, item in enumerate(coffee_times):
        if len(coffee_making) < N:
            coffee_making[idx] = item
        print("coffee_making: ", coffee_making)
        if len(coffee_making) == N:
            temp = True
            while temp:
                for i in range(len(coffee_making)):
                    coffee_making[i] -= 1
                if 0 in coffee_making.values():
                    # temp = [k for k,v in coffee_making.items() if v == 0]
                    # for t in temp:
                    #     result.append(t+1)
                    #     del(coffee_making[t])
                    # print(coffee_making, result)
                    temp = False

# 4

SELECT distinct CARTS.USER_ID from CARTS
LEFT JOIN CART_PRODUCTS
ON CART_PRODUCTS.CART_ID = CARTS.ID
WHERE CART_PRODUCTS.NAME = 'Flour'
ORDER by CARTS.USER_ID;