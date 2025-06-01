# 션이가 가진 N종류의 동전으로 K만큼의 합을 만드려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램 맹들어라.
# 첫째줄엔 N,K가 주어지고 둘째 줄부터 N개의 줄에 동전의 금액이 입력됨

n,k = map(int,input().split())
coins = [int(input().strip()) for _ in range(n)] #리스트 컴프리헨션

# 가장 큰 동전부터 사용하기 위해 내림차순 정렬
coins.sort(reverse=True)

count = 0

for coin in coins:
    if k >= coin:
        count += k // coin
        k %= coin  # 남은 금액 업데이트

print(count)
