class Node:
    def _init_(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
        self.current = None
    
    def addElementHead(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.current = self.head
    
    def addElementTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.current = self.head
    
    def maju(self, steps):
        for i in range(steps):
            if self.current.next is not None:
                self.current = self.current.next
            else:
                break
        return self.current.data
    
    def mundur(self, steps):
        for i in range(steps):
            if self.current.prev is not None:
                self.current = self.current.prev
            else:
                break
        return self.current.data

linkedlist = LinkedList()

linkedlist.addElementHead("Jogja") 
linkedlist.addElementHead("Jakarta") 
linkedlist.addElementTail("Bali") 
linkedlist.addElementTail("Bandung") 

print(linkedlist.maju(2)) 
print(linkedlist.mundur(1)) 
print(linkedlist.maju(5)) 
print(linkedlist.mundur(3)) 