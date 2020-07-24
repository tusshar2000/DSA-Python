def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - (mid + 1) + 1

    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[(mid + 1) + j]
    
    i = 0
    j = 0
    k = left

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i<n1:
        arr[k] = L[i]
        i += 1
        k+=1
    
    while j<n1:
        arr[k] = R[j]
        j += 1
        k+=1

def mergeSort(arr, l, r):
    if l<r:
        mid = (l+r)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)

arr = [4,3,2,1,5,6,8,7]
mergeSort(arr, 0, len(arr) - 1)
print(arr)