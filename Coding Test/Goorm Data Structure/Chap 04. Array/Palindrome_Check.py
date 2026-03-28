class Deque:
    def __init__(self, input_list=None):
        self.items = input_list if input_list is not None else []

    def push_right(self, val):
        self.items.append(val)

    def pop_right(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def push_left(self, val):
        self.items.insert(0, val)

    def pop_left(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)
    
def Palindrome_Check(s):
    s_low = "".join(char.lower() for char in s if char.isalnum())
    # 문자열은 '수정 불가능' 즉 Deque 처리 X
    # list로 변환해 Deque 처리 O
    dq = Deque(list(s_low))
    check = True
    
    while len(dq)>1:
        if dq.pop_left() != dq.pop_right():
            check = False
    return check

sen = input()
print(Palindrome_Check(sen))