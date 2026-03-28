**ML-Fundamentals**

## 📚 References
* **Course:** [Machine Learning for Web Developers (Web ML)](https://www.youtube.com/playlist?list=PLOU2XLYxmsII9mtQ7GmsCD7GkYwS_O6Sg)
* **Provider:** Google for Developers
* **Learning Points:** Basics of TensorFlow.js, Linear Regression, Image Classification, etc.

**[ TensorFlow 사례 ]**

- Object Recognition : Using COCO-SSD → 기능 : 객체의 위치 & 개수 파악 (Image Classification X)
- Speech Command / Audio Detection / Text Toxicity Detection
- Face Mesh → 기능 : 고해상도 얼굴 추적
- Pose Detection : MoveNet & MediaPipe BlazePose

**[ Model 비교 성능 요소 ] → 고객의 요구 사항과 실행 환경에 따라 Model 선정**

- Inference Speed (ms) → 1000ms : 1s / Frames Per Second 방법 : 숫자를 1,000으로 나누기
- File Size (MB) → Method : Chrome 개발자 도구
- Runtime RAM usage (MB) → Method : Chrome 개발자 도구

 **[ Bounding boxes ]** : 4 numbers (정보) → X, Y, Width, Height

**[ Tensor ]**

- Dimension ( 차원 )
    - 0 Dimension : Scalar / Rank 0 Tensor
    - 1 Dimension : Vector / Rank 1 Tensor / tensor1D
    - 2 Dimensions : Matrix / Rank 2 Tensor / tensor2D
    - 3 Dimensions : Rank 3 Tensor / tensor3D → ex) RGB Image
    - 4 Dimensions : Rank 4 Tensor / tensor4D → ex) Video
    - 5 Dimensions : Rank 5 Tensor / tensor5D → ex) Voxel data
    - 6 Dimensions : Rank 6 Tensor / tensor6D → ex) animations
    
    ex) let tensor = tf.tensor1D([1, 2, 3]); → Vector : 3 (3차원) / Tensor : 1 (1차원)
    
- 특징
    - 가비지 컬렉션이 적용 X → tf(변수명).dispose() 사용
    - 비동기 호출 ( 일이 끝날 때까지 기다리지 않고 다음 줄로 넘어가는 것 ) 사용 → await() 사용
- Method of resizing image
    - Crop ( 이미지 자르기 )→ 일부 픽셀 데이터 손실
    - 이미지 크기 조정
        - Resize Bilinear → 확대할 경우, 이미지가 흐릿
        - Resize Nearest Neighbor → 이전에 존재하지 않던 새로운 값을 생성할 때 유용

**[ Single Perceptrons ] - Artificial Neuron**

- Input Function : Inputs * Weights + Bias
- Activation Function : Output & 임계값 비교 → 변환된 값 (이진값) 도출 ex) ReLU
- **[ Linear Regression ] → 예측값 도출**
    - y = w(Weight) * i + b(Bias)
    - 역전파 : 미분을 계산해 가중치를 업데이트 → 오차 ⬇️
    - epoch : 반복 학습의 단위 → 시각화된 학습 곡선 (체크포인트)를 통해 최적의 수를 찾기
    - tf.tidy : 생성된 텐서를 자동으로 정리 ( 예측할 값을 삽입 )

**[ Multi-layer Perceptrons ] - Classification**

- Model Compile 요소 : optimizer, loss function, metrics
- Adam (optimizer) : 학습률을 시간에 따라 자동으로 변경하여 모델이 더 나은 해에 빠르게 수렴 → 이미지 처리에 적합
- Setting Channel
    - Red, Blue, Green Channel → Digit ( 0~1 ) * 255
    - Alpha Channel : 이미지의 투명도를 설정 → 255 (불투명) ⇒ 이미지를 뚜렷하게 보여준다.
    - 캔버스 데이터를 회색조로 설정해야한다.

**[ CNN : Convolutional Neural Network ]**

- Max Pooling : Taking highest numbers ( 2 x 2 pixels ) → 복잡성 감소
- Method : CNN & Max Pooling 반복

**[ Transer Learning (전이학습) ]**

- **정의**
    - 존재하는 데이터셋 (ImageNet)으로 학습된 모델의 가중치를 가져와, 내가 풀고자 하는 문제에 재사용
    - 앞부분은 건드리지 않고, 필터를 통과해 나온 정보들을 어떻게 해석할지의 가중치를 조절해 내 목적에 맞게 최적화
- **구조**
    - 앞부분 (Feature Extractor) : 시각적인 특징 추출 (가중치 고정)
    - 뒷부분 (Classifier) : 추출된 특징을 조합해 판단
- **예시**
    - MobileNet (Full Model): 앞부분 + 뒷부분
    - MobileNetBase (Base Model) : 앞부분