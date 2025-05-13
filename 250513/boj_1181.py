# 1181번
# 알파벳 소문자로 이루어진 N개의 단어를 아래 조건을 만족하게 정렬렬
# - 길이가 짧은 것부터
# - 길이가 같으면 사전순으로
# - 중복된 단어는 중복제거

n = int(input())
words = []

for n in range(n):
    word = input()

    # 중복제거
    if word not in words:
        # 리스트에 추가
        words.append(word)

# 알파벳 길이가 짧은 순으로, 길이가 같다면 사전순으로 정렬
words.sort(key=lambda x: (len(x),x))

# 알파벳 사전순으로 정렬하고, 같으면 길이가 짧은 순으로 정렬 
# words.sort(key=lambda x: (x,len(x)))

for word in words:
    print(word)



