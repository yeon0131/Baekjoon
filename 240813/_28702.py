# FizzBuzz 문제는 
# i = 1, 2, ... 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

# i가 3의 배수이면서 5의 배수이면 “FizzBuzz”를 출력합니다.

# i가 3의 배수이지만 5의 배수가 아니면 “Fizz”를 출력합니다.

# i가 3의 배수가 아니지만 5의 배수이면 “Buzz”를 출력합니다.

# i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력합니다.

# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 
# 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        # 여기에서 else문에 들어오는 값들은 정수일텐데 왜 굳이 리턴값을 str타입으로 지정했는지?
        # 사용자가 입력한 값들이 모두 문자열로 저장되기 때문에 
        # 34번째 줄에서 비교를 할때 같은 문자열이여야 비교가 가능!!
        return str(n)
    
# 세 개의 값 입력받아서 리스트에 저장
arr = [input().strip() for _ in range(3)]

# 시퀀스의 시작점 찾기기
i = 1
while True:
    if[fizzbuzz(i),fizzbuzz(i+1),fizzbuzz(i+2)] == arr:
        break
    i += 1

print(fizzbuzz(i+3))
