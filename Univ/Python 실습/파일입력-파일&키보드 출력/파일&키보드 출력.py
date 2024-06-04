f1=open("Univ/파일입력-파일&키보드 출력/data2.txt", "r") #읽기목적 파일열기
answer = []
for quest in f1 :
    if quest != "" :
        answer.append(input(quest)+"\n")
f1.close()

f2=open("Univ/파일입력-파일&키보드 출력/result2.txt", "w") #쓰기목적 파일열기
f2.write("[응답결과] \n")
f2.writelines(answer)
f2.close()

print("\n[응답 결과]")
for ele in answer : print(ele, end="")