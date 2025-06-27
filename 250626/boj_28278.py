# 28278번(스택2)
# 메모리:99424kb, 시간:572ms
# 스택을 구현한 다음 주어지는 명령을 실행하는 프로그램을 작성하시오.

import sys
from collections import deque

stack = deque()
output = []

for _ in range(int(input())):
    cmd = sys.stdin.readline().strip()
    # if "1 " in cmd:
    if cmd.startswith("1 "):
        stack.append(cmd.split()[1])
    elif cmd == "2":
        output.append(stack.pop() if stack else -1)
    elif cmd == "3":
        output.append(len(stack))
    elif cmd == "4":
        output.append(0 if stack else 1)
    elif cmd == "5":
        output.append(stack[-1] if stack else -1)

sys.stdout.write("\n".join(map(str,output)))