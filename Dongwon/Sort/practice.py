def insertSort(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            # if arr[j] < arr[j-1]:
            #     arr[j],arr[j-1] = arr[j-1],arr[j]
            # else:
            #     break
            if arr[j] > arr[i]:
                temp = arr.pop(i)
                arr.insert(j, temp)
                break
        print(arr)
    
arr = [7,5,9,0,3,1,6,2,4,8]
insertSort(arr)