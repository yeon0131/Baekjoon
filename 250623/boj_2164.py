# 2164번(큐,카드2)
# 메모리:51848kb, 시간:	208ms

# N장의 카드가 차례로 1번이 맨 위에 오도록 놓여있다.
# 제일 위에 있는 카드를 버리고 그다음 카드를 맨 아래로 옮긴다.
# 위 동작을 카드가 한 장 남을 때까지 반복하여 마지막에 남는 카드는?

import sys
from collections import deque

N = int(sys.stdin.readline())
cards = deque()

for i in range(N):
    cards.append(i+1)

# 카드가 한 장 남을 때까지 while문 실행
while len(cards) > 1:
    cards.popleft() # 멘 위 카드 버리고
    cards.append(cards.popleft()) # 그 위 카드는 맨 아래로!

print(cards[0])
