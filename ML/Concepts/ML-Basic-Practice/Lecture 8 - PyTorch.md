import torch
# 행렬 곱 연산
A = torch.rand(5,5)
x = torch.rand(5,1)
A@x # numpy와 유사
# tensors(pytorch) & numpy 메모리 공유
x = torch.ones(5,5)
xn = x.numpy()
xn[4,2] = 10 # x[4,2]도 10을 가진다.

## -- Using the GPU
# GPU 사용 가능 여부 확인
torch.cuda.is_available()
# 설정 (setting)
gpu = torch.device("cuda")
cpu = torch.device("cpu")
# GPU & CPU로 변경
A_gpu = A.to(gpu) # gpu 설정
A_gpu.to(cpu) # cpu로 변경
torch.cuda.empty_cache() # GPU 캐시 비우기

## -- Speedup from GPU
%%timeit # time 측정
# 연산 GPU 사용
A = torch.rand(3000, 3000, device=gpu) 
torch.mm(A,C) # 행렬 곱

## -- Automatic Differentiation (자동 미분)
# y = m*x + c (순전파 : Forward Pass)
x = torch.tensor([2.0])
# requires_grad=True : 모든 계산 과정 꼼꼼히 기록 요청
m = torch.tensor([5.0], requires_grad = True)
c = torch.tensor([2.0], requires_grad = True)
# 오차 측정 (norm : 크기)
loss = torch.norm(y-13) # 13 기준
# grad 측정 (변화량 파악하기 위해서)
m.grad, c.grad
# 역전파 수행
loss.backward()
# 계산 과정 기록 장치 off (with : 영역 설정 (필수))
with torch.no_grad():
# 역전파 수행 (가중치 수정) / 0.01 : 학습률
	m -= 0.01 * m.grad
	c -= 0.01 * c.grad
# 초기화 (필수) -> Backward할 때, 누적됨
m.grad.zero_()
# loss의 개선 과정 관찰
losses += [loss.item()]

## -- Using Library functions
# RELU : 입력값이 음수 -> 0으로 만들기 (정교화)
model = torch.nn.Sequential(
		torch.nn.Linear(5,5),
		torch.nn.ReLU(),
		torch.nn.Linear(5,5))
# MSELoss (*) vs norm 
# 오차의 총합 구하기 (reduction='mean' -> 오차의 평균)
loss_fn = torch.nn.MSELoss(reduction='sum')
# 최적의 가중치 구하기 (Adam)
optimizer = torch.optim.Adam(model.parameters(), lr=0.03)

## -- MNIST Example (이미지 데이터셋)
data = MNIST(".", download=True)
data.train_data[2] # image
data.train_labels[2] # answer

## -- MNIST Training
# 모델 수정 & 손실 출력
for i in range(100):
	y = model(x)
	loss = loss_fn(y,yt)
	loss.backward()
	
	optimizer.step() # 가중치 수정
	optimizer.zero_grad()
	
	losses += [loss.item()]
	print(f"loss = {loss}")
plt.plot(losses)
# 정확도 출력
print("Accuracy = ", (y_pred.argmax(dim=1) == y_test).sum().float().item()/1000.0)
