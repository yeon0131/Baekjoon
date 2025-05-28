# 2752번
# 동규가 갑자기 세수를 하다가 정렬이 하고싶어졌다(???)
# 정수 세 개가 주어졌을 때, 작은 순으로 출력하시오.
# 2 9 5 -> 2 5 9

# 리스트 안의 요소를 문자열 -> 정수로 변환
arr = list(map(int,input().split()))
arr.sort()

for i in range(3):
    print(arr[i],end=' ')

# print(*arr) 으로도 대체 가능