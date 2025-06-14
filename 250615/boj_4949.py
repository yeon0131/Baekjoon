# 4949번(stack, 균형잡힌 세상)
# 메모리:32412kb, 시간:68ms
# 괄호(소괄호,대괄호)의 짝이 맞는지 판단하는 문제

# 여러 줄의 문장에서 각 줄마다 괄호가 짝이 맞는지 확인
# . 한 줄만 입력되면 종료
# 결과는 줄마다 yos/no가 출력됨

import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break

    stack = []
    balanced = True

    for char in line:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if stack:
        balanced = False

    print("yes" if balanced else "no")


# 11번째 줄에서 strip()이 아닌 rstrip()을 쓰는 이유
# 더 명확하고 효율적이기 때문.
# 왼쪽도 검사하는 것이 불필요한 작업이고
# 정확히 필요한 만큼만 처리하려는 습관에서 개발자들은 rstrip()을 쓰는 것임.


# 35번째 줄 "yes" if balanced else "no"
# 삼항 연산자 사용. 구조는 아래와 같음
# A if 조건 else B

# if balanced:
#     print("yes")
# else:
#     print("no")


        