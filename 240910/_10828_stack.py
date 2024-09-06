# 백준 10828번(stack활용)
# push X: 정수 X를 스택에 넣음
# pop: 맨 위 정수 뺀 다음, 그 수를 출력. 비어있으면 -1 출력
# size: 스택에 들어있는 요소 개수 출력
# empty: 스택이 비어있으면 1, 아니면 0 출력
# top: 스택의 가장 위에 있는 정수 출력. 비어있을 시엔 -1 출력
import sys
N = int(sys.stdin.readline())
stack_list = list(sys.stdin.readline().split())
for _ in N :
    if