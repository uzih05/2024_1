line = "홍길동, 컴퓨터공학, 98, 65, 82, 92"
line = line.rstrip() #① 라인 끝의 공백문자들 제거함
print("line.rstrip()의 결과:", line)
line = line.split(',') #② 콤머를 구분자로 부분문자열들로 분리, 리스트 구성함
print("line.split(',')의 결과:", line)
scoreList = []
for i in range(2, len(line)) :
    score = int(line[i]) #③ 수자 부분문자열의 정수형 변환
    scoreList.append(score)
print("line의 수치값 리스트:", scoreList)