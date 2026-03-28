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

def Interval_min(A, n, k):
    result = []
    dq = Deque() # role: index
    
    for i in range(n):
        # 범위를 벗어날 경우
        if not dq.isEmpty() and dq.items[0] <= i-k:
            dq.pop_left()
            
        # 최솟값 구하는 과정
        while not dq.isEmpty() and A[dq.items[-1]] >= A[i]:
            dq.pop_right()
            
        dq.push_right(i)
        
        # 최솟값 append
        if i >= k-1:
            result.append(A[dq.items[0]])
            
    return result

num, length = map(int, input().split())
A = list(map(int, input().split()))
print(*(Interval_min(A, num, length))) # *(unpacking): list의 [] 빼주기