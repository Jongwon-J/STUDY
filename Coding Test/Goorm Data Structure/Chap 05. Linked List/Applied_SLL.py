class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def print(self): # 변경없이 사용할 것!
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")
    
    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def sayNumber(self):
        v = self.head
        total_num = 0
        
        if v is None:
            return 0
        
        while v is not None:
            total_num = total_num * 10 + v.key
            v = v.next
            
        return total_num
        
A = [int(x) for x in input().split()]
L = SinglyLinkedList()
for i in range(len(A)-1, -1, -1):
    L.pushFront(A[i])

a = L.sayNumber()
print(a, type(a) is int)