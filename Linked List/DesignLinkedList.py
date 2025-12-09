class Listnode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Listnode(-1)
        self.tail = Listnode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newnode = Listnode(val)
        newnode.next = self.head.next
        newnode.prev = self.head
        self.head.next.prev = newnode
        self.head.next = newnode
        self.size +=1

    def addAtTail(self, val: int) -> None:
        newnode = Listnode(val)
        newnode.next = self.tail
        newnode.prev = self.tail.prev
        self.tail.prev.next = newnode
        self.tail.prev = newnode
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0
        
        prev = self.head
        curr = self.head.next 
        for _ in range(index):
            prev = curr
            curr = curr.next
        newnode = Listnode(val)
        newnode.prev = prev
        newnode.next = curr
        prev.next = newnode
        curr.prev = newnode

        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size :
            return 
    
        curr = self.head.next
        

        for _ in range(index):
            curr = curr.next

        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)