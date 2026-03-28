def find_median_five(A):
    A.sort()
    return A[len(A)//2]
    
def MoM(A, k): # L의 값 중에서 k번째로 작은 수 리턴
    if len(A) <= 5:
        A.sort()
        return A[k] if k < len(A) else A[-1]
    
    i = 0
    S, M, L, medians = [], [], [], []
    while i+4 < len(A):
        medians.append(find_median_five(A[i: i+5]))
        i += 5
        
    if i < len(A) and i+4 >= len(A): # 마지막 그룹으로 5개 미만의 값으로 구성
        medians.append(find_median_five(A[i:]))

    mom = MoM(medians, len(medians)//2)
    for v in A:
        if v < mom: S.append(v)
        elif v > mom: L.append(v)
        else: M.append(v)
  
    if len(S) > k: return MoM(S, k)
    elif len(S) + len(M) > k: return mom
    else: return MoM(L, k-len(S)-len(M))

# n과 seq를 입력의 첫 줄에서 읽어들인다
n, seq = map(int, input().split())
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
A = list(map(int, input().split()))[:n]
print(MoM(A, seq-1))