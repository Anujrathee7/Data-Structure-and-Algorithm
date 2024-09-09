import sys
def selectionSort(arr):
    index = 0
    for i in range(len(arr)):
        mini = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[mini]):
                mini = j
        arr[i] ,arr[mini]= arr[mini],arr[i]
    
    print(arr)


## In bubble sort we push the maximum elements to the end of array using two loops while in the case of selection sort we select the smallest elements in a iteration and then swap its
## push them to the start of the array

def bubbleSort(arr : list[int]):
    for i in range(len(arr)-1,-1,-1):
        for j in range(0,i):
            if(arr[j] > arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    
    print(arr)


def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1
    
    print(arr)

def mergeSort(arr,low,high):
    if(low < high):
        mid = (low + high) // 2
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)
    
    return

def merge(arr,low,mid,high):
    strIdx = low
    partitionIndex = mid + 1
    temp = []

    while(low <= mid and partitionIndex <= high):
        if(arr[low] <= arr[partitionIndex]):
            temp.append(arr[low])
            low += 1
        else:
            temp.append(arr[partitionIndex])
            partitionIndex += 1
        
    while(low <= mid):
        temp.append(arr[low])
        low += 1
    while(partitionIndex <= high):
        temp.append(arr[high])
        partitionIndex += 1
    
    for i in range(len(temp)):
        arr[strIdx + i] = temp[i]
    
    print(arr)


def quickSort(arr,low,high):
    if(low < high):
        partitionIndex = partition(arr,low,high,low)
        
        quickSort(arr,low,partitionIndex-1)
        quickSort(arr,partitionIndex + 1,high)
        print(arr)

def partition(arr,low,high,pivot):
    while(low <= high):
        if(arr[low] <= arr[pivot]):
            low += 1
        elif(arr[high] > arr[pivot]):
            high -= 1
        else:
            arr[low] , arr[high] = arr[high] , arr[low]

    arr[high] , arr[pivot] = arr[pivot] , arr[high]

    return high  


def largestElement(arr: list[int]) -> None:
    maxi = -sys.maxsize - 1
    for i in range(len(arr)):
        maxi = max(arr[i],maxi)
    
    print(maxi)


def removeDupicate(arr):
    i = 0
    j = 0

    while(j < len(arr)):
        
        if(arr[j] != arr[i]):
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
        j += 1

    print(arr[0:i+1])
    


def leftShift(arr,k):
    temp = arr[0:k]

    for i in range(k,len(arr)):
        arr[i-k] = arr[i]
    
    arr[len(arr)-k:] = temp

    print(arr)

def rightShift(arr,k):
    temp = arr[len(arr)-k:]

    for i in range(len(arr)-k-1,-1,-1):
        arr[i+k] = arr[i]

    
    arr[0:k] = temp

    print(arr)
    

def moveZeros(arr):
    j = -1

    for i in range(len(arr)):
        if(arr[i] == 0):
            j = i
            break
    
    if(j == -1):
        return

    for i in range(j+1,len(arr)):
        if(arr[i] != 0):
            arr[i] , arr[j] = arr[j] , arr[i]
            j += 1
    
    print(arr)

def missingNumber(arr,n):
    xor1 = 0
    xor2 = 0

    for i in range(1,n+1):
        xor1 = xor1 ^ i
    
    for i in arr:
        xor2 = xor2 ^ i
    
    ans = xor1 ^ xor2
    print(ans)


def twoSum(arr,target):
    numsMap = dict()

    for i in range(len(arr)):
        rem = target - arr[i]

        if(rem in numsMap.keys()):
            return (numsMap[rem],i)
        else:
            numsMap[arr[i]] = i

## Creating two functions in python which converts array into singly and doubley linked list

class Node:
    def __init__(self,data) -> None:
        self.data = datax       
        self.next = None

def converArr2LL(arr):
    if(len(arr) == 0):
        return
    
    head = Node(arr[0])

    temp = head

    for i in range(1,len(arr)):
        new_node = Node(arr[i])
        temp.next = new_node
        temp = new_node
    return head

def printLL(head):
    temp = head
    while(temp):
        print(temp.data,end="->")
        temp = temp.next

def middleLL(head):
    slow = head
    fast = head

    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
            
    return slow


def reverseLL(head):
    temp = head
    prev = None

    while(temp):
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    
    return prev


def reverseLLRecursive(head):
    if(head == None or head.next == None):
        return head
    
    newHead = reverseLLRecursive(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newHead



## The most optimal solution will be tortoise solution where you have two pointer slow and fast and slow moves by one while fast moves by two and if slow and fast are the same which 
## means that there is a loop in the linked list 
def detectLoop(head):
    nodeMap = {}

    temp = head

    while(temp):
        nodeMap[temp] = nodeMap.get(temp,0) + 1

        if(nodeMap[temp] > 1):
            return True

        temp = temp.next
    
    print(nodeMap)


head = converArr2LL([1,2,3,4])

detectLoop(head)


