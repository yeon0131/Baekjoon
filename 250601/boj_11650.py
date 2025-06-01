# 11650번(좌표정렬)
# 메모리: 46504kb
# 시간: 2928ms

# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬해라.

n = int(input())
points = []

for i in range(n):
    x,y = map(int,input().split())
    points.append((x,y))

points.sort()
for x, y in points:
    print(x, y)

# 파이썬은 sort()를 이용해서 튜플을 포함한 리스트,문자열,숫자 등 
# 어떤 자료형이든 기본 비교가 가능하면 자동 정렬이 됨.