- **Python 기초 실습**
    
    ```python
    **## -- String Section**
    str1 = "a: %s" % "string" # 출력 형태 : string
    str2 = "b: %f, %s, %d" % (1.0, 'hello', 5) # 데이터의 개수가 많을 때 ()를 이용해 묶는다.
    str3 = "c: {}".format(3.14) # format : 문자열로 변환
    
    **## -- Numpy**
    x @ y # x, y의 행렬곱
    
    **## -- NumPy functions for creating arrays**
    X = np.zeros((10,10)) # 10X10 행렬 안 0으로 생성
    R = np.random.rand(5,5) # 5X5 균등 분포
    R = np.random.randn(5,5) # 5X5 정규 분포
    # start ~ stop까지 num개의 일정한 간격으로 쪼갠다
    np.linspace(start,stop,num)
    
    **## -- Plotting**
    plt.legend(["curve1", "curve2"]) # 범례 표시
    
    **## -- Distinction between numpy 1D arrays and numpy 2D arrays**
    # -1 : 너가 알아서 계산하라는 의미 (다른 부분에 맞춰서)
    X = np.arange(10).reshape(-1,1) 
    X.squeeze() # 차원 크기가 1인 부분만 없애기
    
    **## -- Matrix Creation**
    np.eye(10) # 10X10 단위 행렬 생성 
    np.fliplr(np.eye(10)) # 반대각 행렬 생성 -> 좌우 반전
    np.flipud() # 상하 반전
    np.dot(x,y) # x, y 내적곱 (@와 동일)
    np.diag_indices_from(X) # X의 대각원소만 추출
    
    **## -- Fancy Array Indexing**
    # np.arange()가 index에서 동시에 수행
    X[np.arange(3,9),np.arange(3,9)] = 1
    
    **## -- Reduction operations**
    np.prod(X) # X에 있는 모든 수 곱하기 (prod = product)
    # axis = 0: 수직방향, 1: 수평방향
    np.prod(X, axis=1)
    # X의 상태가 True or False
    np.any(X) # OR 연산
    np.all(X) # AND 연산
    np.cumsum(np.ones((10,10)), axis=1) # 누적합(수평방향)
    
    **## -- Random Numbers**
    import numpy.random as rng
    rng.shuffle(X) # 순서 뒤바꾸기 (in-place)
    rng.permutation(X) # 순서 뒤바꾸기 (new array)
    
    **## -- Linear Algebra in NumPy**
    import numpy.linalg as la
    # 1. 기본 행렬 생성, 기본 연산
    la.eye(3) # 3x3 단위행렬
    la.trace(X) # 행렬 X의 주대각선 원소들의 합
    # 2. 행렬 결합
    la.column_stack((A,B)) # 좌우 결합
    la.row_stack((A,B)) # 상하 결합
    # 3. 선형 방정식 풀이
    la.inv(A) # A의 역행렬
    la.solve(A,b) # Ax = b의 x 추출
    la.lstsq(A,b) # **최소자승법**
    la.pinv(A) # **의사(Pseudo: 가짜) 역행렬**
    # 4. 행렬 분해
    la.qr # **QR 분해**
    la.cholesky # **숄레스키 분해**
    la.svd(A,full) # **특이값 분해**
    # 5. 고유값 & 고유벡터
    la.eig(A) # 일반적인 행렬의 고유값 & 고유벡터 추출
    la.eigh(A) # 대칭 행렬 전용
    la.eigvals(A) # only 고유값
    ```
    
    - List : 다양한 Types O
    - Tuple ( 튜플 ) : 순서 O, Index O, 변경 X
    - Set ( 집합 ) : 순서 X, Index X, 변경 O, 중복 X
    - Dict ( 딕셔너리 ) : 순서 X, Index O, 변경 O, 중복 X