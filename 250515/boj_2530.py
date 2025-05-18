# 2530번(인공지능 시계 문제)
# 입력: 현재 시각 A B C (시, 분, 초)와 요리 시간 D (초 단위)
# 출력: 요리가 끝나는 시각 (시, 분, 초)

import sys

# time_list = list(map(int, input().split()))
# h = time_list[0]
# m = time_list[1]
# s = time_list[2]

# 위와 같이 리스트로 받아서 하나하나 값을 지정하는 것이 아닌
# 한번에 세개의 값을 받아서 지정하기!!!
h, m, s = map(int, input().split())
d = int(input())

# 초 더하기
s += d
m += s // 60
s %= 60

# 분 더하기
h += m // 60
m %= 60

# 시는 24시간제로 맞추기
h %= 24

print(h, m, s)



# split()함수?
# 문자열을 지정한 구분자를 기준으로 쪼개서 리스트로 반환해주는 함수
# 아무것도 안 쓰면 기본 구분자인 공백(띄어쓰기,탭,줄바꿈 등)으로 인식
