import sys

def Quick_Select(A, k):
    if len(A) <= 1:
        return A[0]
    
    pivot = A[0]
    S, L, M = [], [], [] # 독립된 리스트로 생성
    for x in A:
        if x < pivot: S.append(x)
        elif x > pivot: L.append(x)
        else: M.append(x)
        
    if len(S) > k: # S에 존재
        return Quick_Select(S, k)
    elif len(S) + len(M) > k: # M에 존재
        return pivot
    else: return Quick_Select(L, k-len(S)-len(M))

input = sys.stdin.readline # 입력 속도 최적화
# n: 수의 개수, k: 몇 번째로 작은 순서
n, seq = map(int, input().split())
num_list = list(map(int, input().split()))[:n]
print(Quick_Select(num_list, seq-1))