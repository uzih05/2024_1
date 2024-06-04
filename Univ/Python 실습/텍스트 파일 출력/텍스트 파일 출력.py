f1 = open("Univ/Python 실습/텍스트 파일 출력/file.txt", "r")
f2 = open("Univ/Python 실습/텍스트 파일 출력/result5.txt", "w")
f2.write("[write() 함수 출력]\n")
for line in f1 :
        f2.write(line)
f1.close()

f1 = open("Univ/Python 실습/텍스트 파일 출력/data1.txt", "r")
f2.write("\n\n[writelines() 함수 출력]\n")
list1= f1.readlines()
for line in list1 :
    f2.writelines(list1)
f1.close() ; f2.close()