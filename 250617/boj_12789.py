# 12789번 (stack, 도키도키 간식드리미)
# 메모리:32412kb, 시간:44ms
# 줄을 선 학생들을 번호 순서대로 다시 세울 수 있는지 판단하는 문제

n = input()
stack = list(map(int, input().split()))

now = 1
waiting = []

for student in stack:
    if student == now:
        now += 1
    else:
        waiting.append(student)

    while waiting and waiting[-1] == now:
        waiting.pop()
        now += 1

# 스택이 다 비어졌으면 성공
if waiting:
    print("Sad")
else:
    print("Nice")