# 11866번(요세푸스)
# 원을 이루고 있는 N명의 사람에서 K번째 사람을 제거한다.
# 이 과정을 반복했을 때 제거되는 순서를 구하여라.

from collections import deque

N, K = map(int, input().split())

res = []

# 1부터 N까지 들어있는 큐 생성
# circle = deque()
# for i in range(N):
#     circle.append(i+1)

circle = deque(range(1,N+1))

# circle안의 값이 1개 이상일 때 항상 동작
# while len(circle) >= 1:
while circle:
    # K번째 사람이 맨 앞에 오게 회전
    circle.rotate(-(K-1))
    res.append(circle.popleft())

print("<" 
      + ", ".join(map(str,res))
      + ">")