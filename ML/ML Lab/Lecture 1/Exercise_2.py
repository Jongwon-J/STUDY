## Problem 2 : List Comprehensions##
# 1: 0~99까지의 모든 수를 담고 있다.
# 2: 5로 나눴을 때 나머지가 2인 x의 집합
# 3: 짝수인 x의 집합
X = [i for i in range(100)]
s1 = [i for i in X if i % 5 == 2]
s2 = [i for i in X if i % 2 == 0]
s3 = [(x,y) for x in s1 for y in s2]
print(s3)

## Problem 1 : Lists ##
# A = [] # List
# A.append('a')
# A.append('b')
# A.append('c')
# A.insert(1, 'd')
# A.remove('b')
# print(A)