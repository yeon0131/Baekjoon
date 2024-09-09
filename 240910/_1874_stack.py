# 백준 1987번(stack활용)

# 오름차순으로 정렬된 수를 push/pop하면서 주어진 수열을 만드시오.
# push연산은 +로, pop연산은 -로 표현하며 불가능한 경우 NO출력

import sys
n = int(sys.stdin.readline())

stack = []
answer = []  # 출력할 결과 값 (+/-)
flag = False # 예외 발생 여부를 확인할 플래그
cur = 1      # 스택에 넣을 숫자(1~n)

for _ in range(n):
    num = int(sys.stdin.readline())

    while cur<=num:
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')

    else:
        flag = True

if flag == False:
    for a in answer:
        print(a)
else:
    print("NO")

# 성능 요약
# 메모리: 32704KB
# 시간: 164ms


















# 오답노트
# 오름차순된 수열을 push한다고 하여 입력받은 값을 sort하였지만 잘못된 접근방법이였음.
# cur = 1을 이용하여 조건을 만족할 시, cur값을 1씩 증가하도록 만들어야 함.
# 아래는 잘못된 접근 방법으로 푼 문제.
# 백준에 주어진 예제에 대해선 정상적인 출력 값이 나오지만 "출력 초과"라는 결과만 나왔음.
 

#     if num in num_set:
#         print("NO")
#         sys.exit()
#     else:
#         n_list.append(num)
#         num_set.add(num)

# sort_list = list(range(1,n+1))

# stack_box = []
# res = []
# cur = 1 # 1부터 n까지 현재 가르키고 있는 값

# for idx in range(len(sort_list)):
#     ele = sort_list[idx]
#     stack_box.append(ele)
#     res.append('+')

#     # stack_box의 가장 마지막 요소가 n_list의 i번째 요소와 같을 때
#     while stack_box and i < len(n_list) and stack_box[-1] == n_list[i]:
#         stack_box.pop()
#         res.append('-')
#         i+=1

# for r in res:
#     print(r)

    




# sort()함수와 sorted()함수의 차이점

# list.sort()
# sort()메소드는 원본 리스트 내에서 정렬("in-place")하기 때문에 
# 반환 값은 None이 되며 원본 리스트의 내용이 변경됨.

# sorted(list)
# 만약 원본 리스트와 정렬된 리스트를 모두 쓰고 싶다면 sorted()를 사용!!
# sorted() 함수는 정렬된 새 리스트를 반환하면, 원본 리스트를 변경하지 않음.


