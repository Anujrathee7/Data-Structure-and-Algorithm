# Q1: Second Largest Element in an array without sorting
arr = [1,1,2,2,3,3]
def secondLargest(arr):
    largest = -1
    secondLargest = -1
    for i in range(len(arr)):
        if(arr[i] > largest):
            secondLargest = largest
            largest = arr[i]
        elif(arr[i] > secondLargest and arr[i] < largest):
            secondLargest = arr[i]
    
    return (largest,secondLargest)


#print(secondLargest(arr))

# Q2 Check if the array is sorted

def sorted(arr):
    for i in range(1,len(arr)):
        if(arr[i-1] < arr[i]):
            pass
        else:
            return False
        
    return True


#print(sorted(arr))

# Q3 Remove duplicates from sorted array


def removeDuplicate(arr):
    i=0
    for j in range(1,len(arr)):
        if(arr[i] == arr[j]):
            pass
        else:
            arr[i+1] = arr[j]
            i += 1
    print(i)
    return arr[0:i+1] # we are use i+1 because : this does not include the last index element which has the vlaue for example in this case i+1 will give elemts upto i index    

#print(removeDuplicate(arr))


## Q4 Rotating array left in python by d index


"""
[1,2,3,4,5,6,7]  d = 3

"""
arr = [1,2,3,4,5,6,0,0,7]
def rotateArray(arr,rotation):
    total_rotation = rotation % len(arr) 

    temp_arr = arr[0:total_rotation]

    for i in range(total_rotation,len(arr)):
        arr[i-total_rotation] = arr[i]

    arr[len(arr)-total_rotation:] = temp_arr

    return arr


## Move zeros to the end of the array


def moveZeros(arr1):
    j = -1
    for i in range(len(arr)):
        if(arr[i]==0):
            j=i
            break
    
    for i in range(j+1,len(arr)):
        if(arr[i] != 0):
            arr[i] , arr[j] = arr[j],arr[i]
            j +=1


# find the intersection from two sorted arrays

def findIntersection(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    j = 0
    i = 0
    intersection = []
    
    while(i<n1 and j<n2):
        if(arr1[i] > arr2[j]):
            j += 1
        elif(arr2[j] > arr1[i]):
            i += 1
        else:
            intersection.append(arr1[i])
            i += 1
            j += 1

    return intersection

# print(intersection([1,1,2,3,4,5],[1,2,3,4,5,6]))

# find the union from two sorted array

def findUnion(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    j = 0
    i = 0
    union = []
    while(i < n1 and j < n2):
        if(arr1[i] <= arr2[j]):
            if(len(union) == 0 or union[-1] !=  arr1[i]):
                union.append(arr1[i])
            i += 1
        else:
            if(len(union) == 0 or union[-1] != arr2[j]):
                union.append(arr2[j])
            j += 1

    while(j < n2):
        if(union[-1] != arr2[j]):
            union.append(arr2[j])
        j += 1
    
    while(i < n1):
        if(union[-1] != arr1[i]):
            union.append(arr1[i])
        i += 1

## Find missing number in an array of size N-1 containing N-1 numbers between  (Brute force: Use two force loop and check for all the numbers from 1 to N ) Better: Using hashing and creating another array of size N+1 and use it to find the number
## Optimal approach using XOR operator

def find_missing_numbers(arr):
    arrayLength = len(arr)
    xor1 = 0
    xor2 = 0

    for i in range(arrayLength):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (i+1)

    xor2 = xor2 ^ (arrayLength + 1)


## find the longest sub array with given sum (Positive only) brute force: check all the sub arrays in the array and their sum and store the length of the subarray with the desired sum
## Better: Using mathematical X-k , K approach and using this mathematics and hash map try to solve the question
## Optimal: Using 2 Pointers and trying to calculate the desired sum and using conditions to move the pointer

def longestSubArray(arr,k):

    preSumMap = dict()

    sum = 0
    maxi = -1

    for i in range(len(arr)):
        sum += arr[i]
        if(sum == k):
            maxi = max(maxi,i)

        rem = sum - k

        if(rem in preSumMap.keys()):
            length = i - preSumMap[rem] + 1
            maxi = max(length,maxi)        
        
        if(sum not in preSumMap.keys()):
            preSumMap[sum] = i
    
    print(maxi)

## 2 sum problem -> Find the target sum using 2 numbers in a array

def twoSum(arr,k):
    elementsMap = {}

    for i in range(len(arr)):

        counterPart = k - arr[i]

        if(counterPart in elementsMap.keys()):
            return (True,(elementsMap[counterPart],i))
        
        elementsMap[arr[i]] = i
    return False



## sort an array containing 0s, 1s, 2s brute force : use any sorting algorithm to solve the question ## better will be to use hash maps to store the count of 0s , 1s , 2s and then replace all the elemests according to the count
## Optimal solution: Using dutch flag algorithm

def arraySorting(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while(mid <= high):
        if(arr[mid] == 0):
            arr[low] , arr[mid] = arr[mid] , arr[low]
            mid += 1
            low += 1
        elif(arr[mid] == 1):
            mid += 1
        else:
            arr[high] , arr[mid] = arr[mid] , arr[high]
            high -= 1
    
    print(arr)

##arraySorting([2,0,2,1,1,0])


## Majority element inside the array greater than n/2 times Brute force: use two for loops to check for each element and the element which occur more than N/2 times is the answer
## Better will be using hashmap to create a dictionary with the count of the numbers occuring in the array
## Optimal: Using moose voting theorem

def find_majority(arr):
    el = 0
    cnt = 0

    for i in range(len(arr)):
        if(cnt == 0):
            cnt = 1
            el = arr[i]
        elif(arr[i] == el):
            cnt += 1
        else: 
            cnt -= 1
    
    cnt1 = 0

    for i in range(len(arr)):
        if(el == arr[i]):
            cnt1 += 1

    if(cnt1 > len(arr)//2):
        return el
    
#print(find_majority([2,2,1,1,1,2,2]))


## Kade's algorithm to find the maximum subarray sum

def subarray_sum(arr):
    maxi = 0
    sum = 0
    sindex = 0
    eindex = -1
    for i in range(len(arr)):
        sum += arr[i]
        if(sum > maxi):
            maxi = sum
            eindex = i
        if(sum < 0):
            sum = 0
            sindex = i + 1
    
    print((sindex,eindex))
    
    return maxi


#print(subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))


## Best time to buy and sell stocks from array


def stock(arr): 
    mini = arr[0]
    maximumProfit = 0
    for i in range(1,len(arr)):
        cost = arr[i] - mini
        maximumProfit = max(maximumProfit,cost)
        mini = min(mini,arr[i])
    
    print(maximumProfit)



stock([7,1,5,3,6,4])




    






