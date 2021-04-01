N = int(input())

lst = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    else:
        if array[mid] > mid:
            return binary_search(array, start, mid-1)
        else:
            return binary_search(array, mid+1, end)

a = binary_search(lst, 0, N-1)

if a == None:
    print(-1)
else:
    print(a)