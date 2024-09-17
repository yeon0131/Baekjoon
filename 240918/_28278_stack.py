# 백준 28278번(스택 기본 문제)

# 정수를 저장하는 스택을 구현하고 입력으로 주어지는 명령을 처리하라.

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    ele = sys.stdin.readline().strip()

    if ele in '1':
        ele = int(ele.split()[-1])
        stack.append(ele)
    if ele  == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if ele  == 3:
        print(len(stack))
    if ele  == 4:
        if not stack:
            print(1)
        else:
            print(0)
    if ele  == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)

