class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.back = None
    
class doubleyLinkedList():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)

        if(self.head is None):
            self.head = new_node
            return

        last_node = self.head

        while(last_node.next != None):
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.back = last_node
    
    def deleteHead(self):
        if(self.head == None):
            return
        if(self.head.next == None):
            temp = self.head
            self.head = None
            return

        temp = self.head  
        self.head = temp.next
        self.head.back = None
        temp.next = None

    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next


l1 = doubleyLinkedList()


l1.deleteHead()

l1.append(3)

l1.display()
    

    