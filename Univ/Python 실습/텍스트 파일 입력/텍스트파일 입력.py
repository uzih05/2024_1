f1 = open("Univ/Python 실습/텍스트파일 입력/file.txt", "r")
txt = f1.read() # read() 함수 사용
print("read() 반환값:", txt)
f1.close()

f1 = open("Univ/Python 실습/텍스트파일 입력/file.txt", "r")
txt = f1.read(3) # read(n) 함수 사용
print("read(3) 반환값:", txt)
f1.close()

f1 = open("Univ/Python 실습/텍스트파일 입력/file.txt", "r")
txt = f1.readline() # readline() 함수 사용
print("readline() 반환값:", txt)
f1.close()

f1 = open("Univ/Python 실습/텍스트파일 입력/file.txt", "r")
txt = f1.readlines() # readlines() 함수 사용
print("readlines() 반환값:", txt)
f1.close()

print("\nUniv/Python 실습/텍스트파일 입력/file.txt 파일내용 출력")
for element in txt :
    print(element, end ="" )