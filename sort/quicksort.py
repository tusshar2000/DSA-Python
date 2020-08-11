def partition(arr,low, high):
    
    index = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if pivot > arr[j]:
            index += 1
            arr[index], arr[j] = arr[j], arr[index]
    arr[index+1], arr[high] = arr[high], arr[index+1]
    return (index+1)

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi+1, high)

arr = [4,3,25,1,5,6,24,7,69]
quicksort(arr, 0, len(arr) - 1)
print(arr)