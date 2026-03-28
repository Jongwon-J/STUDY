class Stack:
    def __init__(self, max_size = 10):
        self.items = [] * max_size # Stack의 사이즈 선언
        self.idx = -1
        
    def push(self, key):
        self.items.append(key)
        
    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty")
            return None
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)
    
def parChecker(parSeq):
    S = Stack()
    for v in parSeq:
        if v == "(":
            S.push(v)
        else:
            if len(S) == 0:
                return False
            else: # v is ")"
                S.pop()
    
    if len(S) == 0:
        return True
    else:
        return False
    
parSeq = input()
print(parChecker(parSeq))