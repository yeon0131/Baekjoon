# 2751(수 정렬하기2)
# 첫번 째 줄에는 수의 개수, 둘째 줄부터는 n개의 수가 주어진다.
# 단 0<=N<=1000000
# 오름차순으로 정렬되고 수가 중복되지 않도록 출력하시오.

import sys

n = int(sys.stdin.readline())
# nums = []
nums = set()

for _ in range(n):
    num = int(sys.stdin.readline())
    nums.add(num)

nums = list(nums)
nums.sort()

for n in range(len(nums)):
    print(nums[n])


# 오답 풀이 (시간초과과)
# 해당 문제는 십만개 이상의 값이 들어올 수 있기 때문에 시간 초과에 신경을 써야한다.
# 먼저 input()을 sys.stdin.readline()으로 바꿨지만 여전히 시간초과.

# 중복된 값을 피하기 위한 조건인 아래 코드를 바꿔야 함
# if num not in nums

# 리스트에서 in연산 (num not in nums)은 O(N) 시간이 걸림
# 이걸 N번 반복하면 O(N²) 이 돼서 시간 초과💣

# 해결법
# set 사용하기!!
# set은 내부적으로 해시 기반이라 중복 제거 + 빠름 (O(1) 삽입)



