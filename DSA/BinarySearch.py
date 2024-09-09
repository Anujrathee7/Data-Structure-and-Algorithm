import sys

def binarySearch(arr,target):
    low = 0
    high = len(arr) - 1

    while(low < high):
        mid = low + (high - low) // 2

        if(arr[mid] == target):
            return mid
        
        elif(target > arr[mid]):
            low = mid + 1
        
        else:
            high = mid - 1
    
    return 


## Implement lower bound and upper bound

def lowerBound(arr,k):
    ans = -1
    low = 0
    high = len(arr) - 1 

    while(low <= high):
        mid = low + (high - low) // 2

        if(arr[mid] <= k):
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1

    print(ans)


lowerBound([1,2,8,10,11,12,19],0)



        
