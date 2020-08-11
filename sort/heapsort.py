#for explanation
#https://www.youtube.com/watch?v=2DmK_H7IdTo

def heapify(arr, n, i):
    largest = i  #consider root as largest element
    left_child_index = 2*i + 1 
    right_child_index = 2*i + 2

    #check if left child exists, and is greater than root.
    if (left_child_index < n) and (arr[i] < arr[left_child_index]):
        largest = left_child_index
    
    #check if right child exists, and is greater than largest element, here we check with largest element,
    #because we could have swapped if with left in previous operation.
    if (right_child_index < n) and (arr[largest] < arr[right_child_index]):
        largest = right_child_index 
    
    #if root wasn't the largest element, then swap numbers and call heapify at that index.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    #build max-heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    #extract maximum element(root, element), place it at the last indicating sorted from right side, reduce the
    #size of max heap and continue building in this fashion.
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [4,3,25,1,5,6,24,7,69]
heapSort(arr)
print(arr)