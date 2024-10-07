a = []
data = str(input('단어 입력 :'))
while data != '종료' :
    a.append(data)
    data = str(input('단어 입력 :'))
a.sort(reverse=True)
print(a)