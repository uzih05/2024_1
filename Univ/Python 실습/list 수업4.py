lst = []
data = int(input('정수 입력 : '))
while data != -1 :
    insertFlag = False
    for n in range(len(lst)) :
        if data >= lst[n] :
            lst.insert(n, data)
            inserFlag = True
            break
    if not insertFlag :
        lst.append(data)
    data = int(input('정수 입력 : '))
print('결과 리스트 :', lst)
