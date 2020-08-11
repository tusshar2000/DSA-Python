#here assume size of array to be known and element have values be lesser than value of length of array, 
#not good for big sized arrays and numbers

def countSort(arr):
    output = [0 for i in range(10)]
    count = [0 for i in range(10)]
    for i in arr:
        count[i] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    for i in arr:
        output[count[i] - 1] = i
        count[i] -= 1
    return output
arr = [1,2,1,2,4,3,6,1,2,8]
print(countSort(arr))
