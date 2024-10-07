ls = []
data = int(input('정수 입력 :'))
while data != -1:
    ls.append(data)
    data = int(input())

print(max(ls)+min(ls))