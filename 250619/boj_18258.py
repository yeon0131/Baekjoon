# 18258번(큐)
# 메모리:112496kb, 시간:1512ms
# 정수를 저장하는 큐를 구현해라

import sys

# deque를 사용하지 않고 pop메소드를 이용하면 런타임에러가 뜸
from collections import deque

n = int(sys.stdin.readline())
que = deque()

for _ in range(n):
    cmd = sys.stdin.readline().strip()

    if 'push' in cmd:
        que.append(int(cmd.split()[1]))

    elif cmd == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())

    elif cmd == 'size':
        print(len(que))

    elif cmd == 'empty':
        if not que:
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])

    elif cmd == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])


# 문제핵심
# 1. input()대신에 sys.stdin.readline()쓰기
# 2. pop구현할 때 pop(0)으로 값을 삭제하는 것이 아닌
#    collections.deque를 활용, popleft()로 시간복잡도 문제 없음