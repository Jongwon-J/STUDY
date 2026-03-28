import numpy as np

# Step 1: 변수 설정
n = int(input())
M = np.random.rand(n,n)
A = M + M.T # M.T = np.transpose(M) # A: 대칭행렬
v = np.random.rand(n) # v: 벡터
l = 0
old_l = -1

# Step 2 : 반복문을 이용한 벡터 업데이트
while abs(l - old_l) > 1e-9:
    old_l = l
    
    v = np.dot(A, v)
    v = v / np.linalg.norm(v)
    l = v.T @ A @ v

true_evals, true_evecs = np.linalg.eigh(A)
print(f"내가 구한 최대 고윳값 {l:.1f}\n")
print(f"넘파이 정답 최대 고윳값 {true_evals[-1]:.1f}")
    