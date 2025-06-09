# 1541번(잃어버린 괄호,Greedy)
# 숫자, +, - 로 이루어진 식에 적절히 괄호를 쳐서
# 식의 결과를 최소로 만들어라.

expression = input().split('-')
res = 0

for i, group in enumerate(expression):
    nums = sum(map(int, group.split('+')))
    if i == 0:
        res += nums
    else:
        res -= nums

print(res)


# enumerate함수?
# 리스트 같은 걸 반복할 때, 인덱스와 값을 동시에 꺼내주는 파이썬 내장함수
