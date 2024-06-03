def rev(word):
    rev_word = "" # 빈 문자열 초기화
    
    for char in word : # 역순으로 만들기
        rev_word = char + rev_word
    
    return rev_word

input = input("영문 단어를 입력하세요: ") # 사용자로부터 영문 단어를 입력

reversed = rev(input)
print("입력된 단어의 역순:", reversed)
