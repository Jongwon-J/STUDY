- **Scikit-learn**
    - Regression : 수치 ( 연속적인 숫자 ) 예측
        - Ex ) 내일의 기온 예측, 화장품 성분 농도에 따른 피부 수분도 예측
    - Clustering (군집화) & Classification (분류) : 카테고리 분류 & 예측
        - Ex ) 분류 (지도 학습) : 이 꽃은 벚꽃인가, 무궁화인가? / 군집화 (비지도 학습) : 구매 패턴 비슷한 고객끼리 자동으로 그룹핑
    - Dimensionality reduction : 우리가 데이터를 시각화할 수 있도록 저차원으로 변경

## -- Regression (수치 예측)
from sklearn import linear_model
# model.coef_ : 기울기, model.intercept_ : y절편
print(model.coef_, model.intercept_)
# 모델 성적 확인 (0~1 / 1에 가까울수록 예측 잘함)
model.score(X, y)
# 선형성
df.plot('sepal_length', 'petal_length', kind='scatter')
sepal_length = np.linspace(0,3,10).reshape(-1,1)
plt.plot(sepal_length, model.predict(sepal_length), 'r')
# 비선형성
sepal_length = np.linspace(0,3,10).reshape(-1,1)
root_length = np.sqrt(sepal_length)
# sepal, root_length 특성 모두 고려
features = np.hstack((sepal_length, root_length))

## -- Classification (카테고리 나누기)
from sklearn import datasets
# DESCR 함수를 통해 데이터셋의 설명 관찰
print(iris.DESCR)
# train, test 데이터 나누기 (random_state : 섞이는 방식 번호)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# 분류
from sklearn.neighbors import KNeighborsClassifier
# n_neighbors -> 몇 명의 이웃을 볼 것인가 (거리 기준)
model = KNeighborsClassifier(n_neighbors=5)

## -- Evaluating your model
# test model 정확도 평가 방법 1
np.mean(model.predict(X_test) == y_test) # Accuracy
# test model 정확도 평가 방법 2
import sklearn.metrics as metrics
metrics.accuracy_score(model.predict(X_test), y_test)
# 평가 보고서
metrics.classification_report(model.predict(X_test), y_test)
# Cross validation (교차 검증)
from sklearn.model_selection import cross_val_score
model = KNeighborsClassifier()
# cv: 등분
scores = cross_val_score(model, X, y, cv=5)

## -- Exercise
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
# 1. 모든 모델을 리스트에 담기
models = {
    "MLP (인공신경망)": MLPClassifier(max_iter=1000, random_state=0),
    "SVC (SVM)": SVC(),
    "Gaussian Process": GaussianProcessClassifier(),
    "Decision Tree": DecisionTreeClassifier(random_state=0),
    "Random Forest": RandomForestClassifier(random_state=0),
    "AdaBoost": AdaBoostClassifier(random_state=0),
    "Gaussian NB": GaussianNB(),
    "QDA": QuadraticDiscriminantAnalysis()
}

# 2. 반복문을 돌며 학습 및 평가
results = []

for name, model in models.items():
    model.fit(X_train, y_train) # 학습
    y_pred = model.predict(X_test) # 예측
    
    # 통계치 계산
    acc = accuracy_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred, average='macro')
    rec = recall_score(y_test, y_pred, average='macro')
    
    results.append([name, acc, pre, rec])

# 3. 결과 출력
df_res = pd.DataFrame(results, columns=['Model', 'Accuracy', 'Precision', 'Recall'])
print(df_res.sort_values(by='Accuracy', ascending=False))

## -- Clustering (비지도 학습)
from sklearn.cluster import KMeans
# K(n_clusters) : 몇 개의 그룹으로 나눌지
model = KMeans(n_clusters=3, random_state=0)
model.labels_ # 모델이 추측한 그룹
iris.target # 실제 정답
# 산점도 표현
for name in [0,1,2]:
	plt.scatter(X[model.labels_ == name, 0], X[model.labels_ == name, 1], label = name)
	
## -- Dimension Reduction (비지도 학습)
from sklearn.manifold import TSNE
model = TSNE(n_components=2) # 2차원으로 변경 (준비)
# 4차원 Data X를 넣어서 fit하고 2차원으로 변환 (실제 압축)
X_transformed = model.fit_transform(X) 