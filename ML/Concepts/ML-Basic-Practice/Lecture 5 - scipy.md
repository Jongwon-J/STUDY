```python
**## -- Interpolation : scipy.interpolation**
import scipy.interpolation as interp
plt.plot(x,y,'bo') # 'bo' : blue + circle (파란 원)
f = interp.interp1d(x,y,kind="linear") # 보간
f(0.2) # kind에 따라 함수 식 계산
# kind -> zero: 계단식 linear: 선, cubic: 곡선
# 형태 : plt.plot(x좌표, y좌표)
# 괄호가 두 개 나오는 이유는 interp...()가 f라는 함수 역할
plt.plot(x_fine, interp.interp1d(x,y,kind="zero")(x_fine))

**## -- Optimization : scipy.optimize => 최적화**
from scipy import optimize
# 목표 수치를 가장 낮게 만드는 입력값을 찾아주는 탐색기
optimize.minimize(함수, 탐색 시작 좌표)
X, Y = np.meshgrid(x,y) # 2차원 평면의 모든 좌표를 채운 모눈종이
plt.imshow(f(np.array([X,Y]))) # 등고선

**## -- Curve Fitting** 
# f가 x,y에 잘 맞도록 a,b를 조절 
****((a,b),_) = optimize.curve_fit(f,x,y,(0,0)) 

**## -- Root Finding => 해 찾기**
optimize.root(f,-1) # 0이 되는 지점 찾기 (-1 근처)

**## -- Statistics : scipy.stats => 통계**
from scipy import stats
****stats.norm.fit(samples) # 정규분포 추출 (평균, 표준편차)
****stats.ttest_ind(a,b) # 독립표본 T-검정 수행
2*np.random.randn(1000)+5 # 평균 5, 표준편차 2인 데이터 모임
# 확률 밀도 함수 : 데이터의 전체적인 흐름을 대략적으로 추정
pdf = stats.kde.gaussian_kde(x)

**## -- Numerical Integration : scipy.integrate => 적분**
import scipy.integrate as integ
integ.quad(f,-1,1) # -1~1까지 정적분
# 초깃값 (위치:1,속도:1)에서 f라는 함수를 지키며 시간 t에 따라 모든 발자취를 기록하는 함수
Y = integ.odeint(f,[1,1],t)
```

- **Interpolation (보간)** : 데이터 사이를 메꾸는 것
- **Extrapolation (외삽)** : 데이터 범위 밖의 미래 값을 예측하는 것

**[ Optimize (최적화)]**

- 한정된 자원으로 최고의 가성비를 뽑아내는 것
- Q. # import scipy.optimize as opt 이런 식으로 작성하지 않는 이유? → optimize로도 직관적이기 때문에 굳이 줄이는 선택 X
- **optimize.minimize(함수, 탐색 시작 좌표)** : 탐색 시작 좌표에서 시작해 낮은 곳 쪽으로 이동
- **X, Y = np.meshgrid(x,y)** : X → x좌표 구성 ( 각 열끼리 수가 동일 ), Y → y좌표 구성 ( 각 행끼리 수가 동일 )
- **plt.imshow()** : x,y 좌표가 실제 좌표가 아닌 index를 가리킨다.
    
    **[ optimize.minimize() 함수 결과 분석 ]**
    
    - **fun** : 함수의 최솟값, **x** : 최적의 입력값
    - **nit** : 반복 횟수, **nfev** : 함수 계산 횟수
    - **jac** : 기울기 ( 0에 가까울수록 정밀 )
    - **hess_inv** : 곡률 ( 수 ⬆️ ⇒ 완만 / 1.0 근처 : 표준적인 곡률 )
    
    ![스크린샷 2026-03-22 오후 4.49.25.png](attachment:eab643d7-2b73-419c-8eca-e449961dd066:스크린샷_2026-03-22_오후_4.49.25.png)
    

**[ Curve fitting (곡선 적합) ]**

- 흩어져 있는 데이터 점들을 가장 잘 설명하는 하나의 매끄러운 선을 찾는 과정
- **((a,b),_) = optimize.curve_fit(f,x,y,(0,0))** : 반환값 1 → 최적값, 반환값 2 → 신뢰도 / (0,0) → 초깃값

**[ Root Finding (수치적 해 구하기) ]**

- $f(x)=0$을 만족하는 $x$를 찾는 것
    
    **[ optimize.root(f, -1) 함수 결과 분석 ]**
    
    ![스크린샷 2026-03-24 오후 7.33.05.png](attachment:ebb87c5e-c6c9-4b2f-b2a9-8c523928f69b:스크린샷_2026-03-24_오후_7.33.05.png)
    
    - **status : 1**  → 최종 상태 코드 ( 1: 아무 문제 없이 해 완벽 찾음 )
    - **r & qtf** → QR 분해 관련 값 ( 나중에 학습 )
    - $A_{ub}$ : Upper Bound → 상한선
    - $A_{eq}$ : Equality → 등호

**[ scipy.stats (통계) ]**

- **t_stat, p_value = stats.ttest_ind(a,b)**
    - **t_stat (T-score)** : 두 그룹의 평균이 얼마나 멀리 떨어져 있는지 나타내는 수치
    - **p_value** : 차이가 ‘우연히’ 발생할 확률 ( 0.05 미만 → 통계적으로 유의미 )
- **n, bins, patches = plt.hist(x, bins=10)**
    - **n** : Counts ( 빈도수 )
    - **bins** : Edges ( 구간 경계 )
    - **patches** : 그래픽 객체 ( 막대기 그림 )

**[ Numerical Integration : scipy.integrate ]**

- **quad** : Quadrature(구적법)의 약자로, 곡선 아래의 면적을 구하는 함수
- **result, error = integ.quad(f,-1,1)**
    - **result** : 적분값
    - **error** : 예상 절대 오차 (실제 정답과 최대 얼마나 차이 나는지)
- **Y = integ.odeint(f,[1,1],t)** → Y[시간, [0]:위치 / [1]:속도]

**[ Physical Simulation : 포물선 운동 ]**

**[ Other Useful Packages ]**

- **networkx** : 네트워크(그래프) 데이터 구조
    - **G.add_nodes_from([1,2,3,4])** : 번호가 1,2,3,4인 노드들을 한꺼번에 생성
    - **G.add_edge(1,2)** : 번호가 1번인 노드가 2번이 노드와 연결
    - **nx.complete_graph(10)** : 노드 10개를 생성하고 서로 모두가 연결되게 하는 그래프
- **sympy** : 기호 다루는 라이브러리 ( $$ $$ )
    
    ```python
    x,y = symbols("x y") # 기호 형태 만들기
    expand(x*expr) # 식 전개 (괄호 풀기)
    factor(x**2 - 2*x*y + y**2) # 인수분해
    latex(expr) # 기호 식 -> 문자열
    simplify((x-y)**2 + (x+y)**2) # 최적화 (가장 짧은 모양 찾기)
    sub(y,1/(1+x)) # y -> 1/(1+x)로 대체
    evalf(subs={'x':2, 'y':4}) # x=2, y=4로 대체해 계산
    Integral(식, dx범위, dy범위) # 적분식
    I.doit() # 직접 계산
    series(변수, 근처값, 몇 차) # 테일러 급수 표현 
    ```