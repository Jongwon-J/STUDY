# 1. class Node 선언 부분
class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self
    def __str__(self):
        return str(self.key)

# 2. class DoublyLinkedList 선언부분
class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # create an empty list with only dummy node

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
            
    def __str__(self):
        return " -> ".join(str(v.key) for v in self)
    
    def printList(self):
        v = self.head.next
        print("h -> ", end="")
        while v != self.head:
            print(str(v.key)+" -> ", end="")
            v = v.next
        print("h")
        
    def splice(self, a, b, x): # a:b까지의 노드를 x 뒤에 붙인다
        if a == None or b == None and x == None:
            return None
        
        # cut
        a.prev.next = b.next
        b.next.prev = a.prev
        
        # paste
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a
        
    def moveAfter(self, a, x):
        return self.splice(a, a, x)
    
    def moveBefore(self, a, x):
        return self.splice(a, a, x.prev)
    
    def insertBefore(self, x, key):
        return self.moveBefore(Node(key), x)
    
    def insertAfter(self, x, key):
        return self.moveAfter(Node(key), x)
    
    def pushFront(self, key):
        return self.insertAfter(self.head, key)
    
    def pushBack(self, key):
        return self.insertBefore(self.head, key)
    
    def deleteNode(self, x):
        if x == None or x == self.head:
            return None
        x.prev.next, x.next.prev = x.next, x.prev
        
    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key
    
    def popBack(self):
        if self.head.prev == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        return key
        
    def search(self, key):
        v = self.head.next
        while v != self.head:
            if v.key == key:
                return v
            v = v.next         
        return None
    
    def isEmpty(self):
        return self.head.next == self.head
    
    def first(self):
        if self.head.next == self.head:
            return None
        else:
            return self.head.next
    
    def last(self):
        if self.head.prev == self.head:
            return None
        else:
            return self.head.prev
        
    def join(self, list):
        return self.splice(list[0], list[len(list)-1], self.head.prev)
    
    def split(self, x):
        if x is None or x == self.head:
            return None

        # 새 리스트 만들기
        new_list = DoublyLinkedList()

        # 연결 범위: x ~ self.head.prev (즉, 끝까지)
        a = x
        b = self.head.prev
        self.splice(a, b, new_list.head)  # dummy 뒤에 붙이기

        return new_list
        
        
L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")