# 1427번(정렬)
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. 
# 그 수의 각 자리수를 내림차순 정렬하여 출력해라.

n = input()
digits = list(map(int,str(n)))
digits.sort(reverse=True)

for digit in digits:
    print(digit,end='')
