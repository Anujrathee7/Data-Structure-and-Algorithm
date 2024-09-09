def mergeSort(arr, low ,high):
    mid = (low + high) // 2
    if(low >= high):
        return

    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    tempArr = []
    left = low
    right = mid + 1

    while(left <= mid and right <= high):
        if(arr[left] <= arr[right]):
            tempArr.append(arr[left])
            left += 1
        else:
            tempArr.append(arr[right])
            right += 1
    
    while(left<=mid):
        tempArr.append(arr[left])
        left += 1
    while(right <= high):
        tempArr.append(arr[right])
        right += 1
    for i in range(low,high+1):
        arr[i] = tempArr[i-low]






def quickSort(arr,low,high):
    if(low < high):

        partitionIndex = partition(arr,low,high) 

        quickSort(arr,low, partitionIndex-1)

        quickSort(arr,partitionIndex+1,high)

  
def partition(arr,low,high):
    pivot = arr[low]

    i = low

    j = high

    while(i < j):
        while(arr[i] <= pivot and i <= high - 1):
            i += 1
        while(arr[j]>pivot and j >= low + 1):
            j -= 1
        if(i<j):
            arr[i] , arr[j] = arr[j] ,arr[i]
    
    arr[low] , arr[j] = arr[j] , arr[low]

    return j



    
    


arr = [33,44,1,6,3,3,4,33]

quickSort(arr,0,len(arr)-1)

print(arr)
