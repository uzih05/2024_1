def count(sen):
    words = sen.split() # 공백을 기준으로 문장 분할.

    count = len(set(words)) # 단어의 개수를 저장할 변수를 초기화.
    
    return count

input = input("문장을 입력하세요: ")

print("문자열의 개수:", count(input))

