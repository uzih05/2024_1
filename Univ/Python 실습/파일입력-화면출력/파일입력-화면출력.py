f1 = open("Univ/Python 실습/data1/data1.txt", "r")  # 파일개방
print("-" * 20)
txt = f1.read(1)  # 파일사용: read() 함수이용
while txt != "" :
    print(txt, end="")  # Add end="" to avoid double new lines
    txt = f1.read(1)  # 파일사용
print()
print("-" * 20)
f1.close()  # 파일폐쇄