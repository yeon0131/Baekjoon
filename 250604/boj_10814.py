# 10814번(나이순 정렬)
# 나이가 적은순으로, 같다면 먼저 가입한 순으로 정렬하시오.

n = int(input())
points = []

for _ in range(n):
    x,y = input().split()
    points.append((int(x),y))

points.sort(key=lambda point:point[0])

for x,y in points:
    print(x,y)


# key = lambda point:point[0] 해석
# key =             해당함수(sort)에 대한 key값 지정.
#                   sort() 함수에서 정렬 기준을 지정할 때 쓰는 매개변수수
# lamda             익명 함수를 만들 때 사용하는 키워드
#                   def없이 간단한 함수를 1줄로 만들 수 있음
# point : point[0]  f(x)=x[0] 같은 느낌
#                   x:x+1 이면 f(x)=x+1같은거임.
