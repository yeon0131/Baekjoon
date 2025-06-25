# 28279번(덱2)
# 메모리:87888kb, 시간:588ms
# 정수를 저장하는 덱을 구현한다음 입력으로 주어지는 명령을 처리하는 프로그램을 만드시오

import sys
from collections import deque
dq = deque()

# input()을 sys.stdin.readline()으로 최적화한 것처럼
# print()도 출력에 최적화(안했을 시엔 시간 840ms걸림)
output = []

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    cmd = input().strip()
    if "1 " in cmd:
        dq.appendleft(cmd.split()[1])
    elif "2 " in cmd:
        dq.append(cmd.split()[1])
    elif cmd == "3":
        # if dq:
        #     print(dq.popleft())
        # else:
        #     print(-1)
        output.append(dq.popleft() if dq else -1)
    elif cmd == "4":
        output.append(dq.pop() if dq else -1)
    elif cmd == "5":
        output.append(len(dq))
    elif cmd == "6":
        output.append(0 if dq else 1)
    elif cmd == "7":
        output.append(dq[0] if dq else -1)
    elif cmd == "8":
        output.append(dq[-1] if dq else -1)

# output에 모아놓은 값을 한번에 출력해서 출력에 최적화함
sys.stdout.write('\n'.join(map(str,output)))