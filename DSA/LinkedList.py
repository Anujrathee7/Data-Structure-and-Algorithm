class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)

        if(self.head is None):
            self.head = new_node
            return
        
        last_node = self.head

        while (last_node.next):
            last_node =  last_node.next
        last_node.next = new_node
    
    def display(self):
        current_node = self.head

        while(current_node):
            print(current_node.data,end="->")
            current_node = current_node.next
    
    def deleteHead(self):
        if(self.head is None): return "Linked List is empty"
        temp = self.head
        self.head = self.head.next
        del temp
    
    def deleteK(self,k):
        if(k==1):
            self.deleteHead()
        
        temp = self.head
        prev = None

        cnt = 0

        while(temp != None):
            cnt += 1

            if(cnt == k):
                prev.next = prev.next.next
                temp.next = None
                del temp
                break

            prev = temp
            temp = temp.next

    def deleteElement(self,el):
        if(self.head.data==el):
            self.deleteHead()
        
        temp = self.head
        prev = None

        while(temp != None):

            if(temp.data == el):
                prev.next = prev.next.next
                del temp
                break

            prev = temp
            temp = temp.next
    
    def insertAtHead(self,el):
        temp = Node(el)
        temp.next = self.head

        self.head = temp
    def insertAtTail(self,el):
        temp = self.head
        while(temp.next):
            temp = temp.next
        
        temp.next = Node(el)

    def insertAtK(self,el,k):        
        if(k == 1):
            self.insertAtHead(el)
            return

        temp = self.head
        cnt = 0

        while(temp.next  != None):
            cnt += 1
            if(cnt == (k-1)):
                new_node = Node(el)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next



    


"""def converArr2LL(arr):
    if(len(arr) == 0): return None
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        new_node = Node(arr[i])
        temp.next = new_node
        temp = new_node
    

    return head

def printLL(head):
    while(head):
        print(head.data,end=", ")
        head = head.next

def removeHead(head):
    if(head is None): return head
    temp = head
    head = head.next
    del temp
    return head

def removeTail(head):
    if (head == None or head.next == None): 
        del head
        return None
    temp = head
    while(temp.next.next != None):
        temp = temp.next
    del temp.next
    temp.next = None
    return head
"""
l1 = linkedList()

l1.insertAtK(5,1)

l1.display()


    
        