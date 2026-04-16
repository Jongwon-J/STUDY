- **Pandas**
    - **Characteristic**
        - Working with missing data
        - Time series-specific functionality
        - Normal table operations → Merging & Joining, Groupby

import pandas as pd
import numpy as np

## -- Object & Basic Creation
pd.Series(data, index = index) # 1D
pd.DataFrame # 2D
pd.Panel # 3D

## -- Series
pd.Series(data, index = index) # 1D
# [] : list, {} : dictionary
d = {'a':[0., 0], 'b':{'1': 1.}, 'c': 2.}
# Broadcasting : 모든 인덱스에 값을 복사
pd.Series(0, index = ['a','b','c','d','e'])
# Label Matching : 인덱스 이름이 창고(data)에 있는지 대조
# d에 index 'a','b','c'만 설정되어 있어서 'd','e': NaN
pd.Series(d, index = ['a','b','c','d','e']) 
# Conditional Max - Index with Booleans : 조건에 맞는 데이터 뽑아내기
print(s[s > s.mean()], end = end_string)
# Elementwise Function - Vectorization : 모든 숫자에 똑같은 계산 한 번에 적용
print(np.exp(s), end = end_string)
# Check for index label
print('f' in s, end = end_string)
# Get item with index 'f' (없으면 None)
print(s.get('f', None), end = end_string)

## -- Series Attributes
# items로 list index, value값 접근
for idx, val in s.items():
	print(idx,val)
s.sort_index() # index 오름차순
s.sort_value() # value 오름차순
s.value_counts() # value별 개수 check
s.value_counts().head(5) # 상위 5개 선별 (slicing도 가능)

## [ DataFrame ] - 데이터를 표로 만드는 라이브러리
# 기본 구조
df = pd.DataFrame(data, index = index, columns = columns)
## -- From dict of series or dicts
# one, two: columns / a, b, c, d: index
d = {'one': pd.Series([1,2,3], index = ['a','b','c']),
	'two': pd.Series(list(range(4)), index = ['a','b','c','d'])}
df = pd.DateFrame(d)

## -- From dict of ndarray / lists
# index 설정 안 할 경우, 0,1,2,3 순으로 기본 설정
d = {'one': [1.,2.,3.,4], 'two': [4.,3.,2.,1]}

## -- From a list of dicts
data = [{'Columns'+str(i):np.random.randint(100) for j in range(5)}]
# Get only certain columns
df = pd.DataFrame(data, columns = ['Column0', 'Column1'])

## -- Attributes
df.shape # DataFrame의 행,열 구성
df.values # DataFrame's values
df.insert(Loc, Column(Name), Value) # 삽입
df.pop('three') # 특정 열 추출(빼기)

## -- Indexing and Selection
df[col] # Select Column -> Series
df.loc[label] # Select Row -> Series
df.iloc[idx] # Select Row -> Series
df[1:3] # Slicing (Index) -> DataFrame
df[df['one']>2] # df[mask] -> DataFrame

## -- Simplest form of Indexing: []
# 짝수로 설정 / 위, 아래 동일한 개수 보여줘야 한다.
pd.options.display.max_rows = 4  
df.loc(label, col) # Row, Col -> DataFrame
df[df['A'] > df['B']].head() # boolean mask
df['A'] # df.A와 동일

## -- Selecting by label .loc
df.loc[:, df['2000-01-01']>0] # 특정 행이 0보다 큰 열 추출
df.loc[:, (df>0).all()] # 모든 행이 0보다 큰 열만 추출

## -- Selecting by position
# index: 0,1,2 -> 0,2,4 / col: 0,1,2 -> 0,3,6
df = pd.DataFrame(np.random.randn(6,4), index=list(range(0,12,2), columns=list(range(0,12,3)))
# Select via integer mask
boolean_mask = df1.iloc[:,1] > 0.0
# iloc 괄호 안에 True,False 들어갈 수 있다.
df1.iloc[boolean_mask.values,1]

## -- Merging DataFrames
# Standard
pd.merge(left, right, how='inner', on=None, 
left_on=None, right_on=None, left_index=False, right_index=False, sort=True)
merged = pd.merge(left, right, how='outer')

## -- Function Application
# Apply to each column
df1.apply(np.mean) # axis = 0 (default)
# Apply to each row
df1.apply(np.mean, axis = 1) # 열 방향으로 하나씩 계산

## -- lambda function
# normalize columns
df1 = df1.apply(lambda x: (x- x.mean())/x.std(), axis = 0)
# apply() = applymap()
df1.apply(lambda x: x.idxmax()) 

## -- I/O Functions
# Loading data from CSV
pd.read_csv / pd.to_csv
pd.read_excel / pd.to_excel
pd.read_sql / pd.to_sql
# pickle : python 전용 바이너리 형식인 피클 파일
pd.read_pickle / pd.to_pickle
# 데이터 분석 (행,열 개수 & 인덱스 범위, 
# 각 컬럼별 세부 정보 (결측치가 아닌 데이터의 개수), 데이터 타입)
iris_data.info()
# Dataframe 설명 & 요약
iris_data.describe()

## -- The split/apply combo (groupby)
df = pd.DataFrame({'key' : ['A','B','C','A','B','C','A','B','C'],
									 'data' : [0,5,10,5,10,15,10,15,20]})
# .agg : aggregate의 약자로, 여러 개의 데이터를 하나로 뭉쳐 계산
sums = df.groupby('key').agg(np.mean)

## -- Plotting data
import matplotlib.pyplot as plt
df.plot() # 그림의 표현 구현 단계 (label, title)
plt.show() # 그림 출력
# 수평선 긋기 (y축 위치, 선의 색상)
plt.axhline(0, color='k')
# axes : Data type (plot), ax : data 변수 이름 /
# dict : 박스의 수치 데이터, both : 그림 & 수치 데이터
ax = iris_data.groupby('species') \
         .get_group('setosa') \
         .boxplot(column=["sepal_length","sepal_width"], return_type='axes')