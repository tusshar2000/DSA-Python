def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        index = i
        for j in range(i+1, length):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr
print(selection_sort([2,5,3,1,67,43]))
