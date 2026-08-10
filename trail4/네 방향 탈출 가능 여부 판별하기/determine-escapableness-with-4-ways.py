from collections import deque

def push(x, y):
    global order
    
    answer[x][y] = order
    order += 1
    visited[x][y] = True
    q.append((x,y))

def in_range(x, y):
    return 0 <= x and x < N and \
           0 <= y and y < M
           
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or A[x][y] == 0:
        return False
    return True
    
def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        if x == N-1 and y == M-1:
            return 1
        
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            
            if can_go(new_x, new_y):
                push(new_x, new_y)
                
    return 0
    
# -------- main -----------------------
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

answer = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
q = deque()
order = 1

push(0, 0)
print(bfs())