def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        made_swaps = False
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                made_swaps = True
        if not made_swaps:
            break
    return arr

print(bubble_sort([2,131, 69,3,4,5]))