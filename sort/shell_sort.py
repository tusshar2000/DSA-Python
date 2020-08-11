def shellSort(arr): 

    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j-gap] > key:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = key 
        gap //= 2


arr = [ 12, 34, 54, 2, 3] 
shellSort(arr)
print(arr)
