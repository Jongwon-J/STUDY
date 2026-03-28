import time, random

def prefixSum1(X, n):
    S = [0] * n  
    for i in range(n):
        for j in range(i+1):
            S[i] += X[j]
    return S
	
def prefixSum2(X, n):
    S = [0] * n
    S[0] = X[0]
    for i in range(1, n):
        S[i] = S[i-1] + X[i]
    return S
	
random.seed()   # Reset random function
n = int(input())    # Get n
# Fill list X with n random numbers by calling randint
X = []
for _ in range(n):
    X.append(random.randint(-999,999))
    
# Call prefixSum1 & Check execution time
before = time.process_time()
prefixSum1(X, n)
after = time.process_time()
print(f"{after - before:.6f}")

# Call prefixSum2 & Check execution time
before = time.process_time()
prefixSum2(X, n)
after = time.process_time()
print(f"{after - before:.6f}")