import numpy as np
from scipy.optimize import linprog

# 1. 목적 함수 계수
c = [1,2]

# 2. 부등식 제약 조건
A_ub = [[1,0],
        [-5,-1]]
b_ub = [1,0]

# 3. 등식 제약 조건
A_eq = None
b_eq = None

# 4. linprog 실행
res = linprog(c, A_ub, b_ub, bounds=(None,None))