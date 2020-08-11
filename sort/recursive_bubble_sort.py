def recursive_bubble_sort(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            return arr
        if arr[i+1] < arr[i]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            recursive_bubble_sort(arr)
    return arr
print(recursive_bubble_sort([2,5,3,1,67,43]))