f2 = open("Univ/Python 실습/키보드입력-파일출력/result.txt", "w")
txt = input("남기고 싶은 메시지하세요?\n")
# for i in range(3) :
while txt !='.' :
    f2.write(txt) # write()함수 이용
    txt = input()
f2.close()