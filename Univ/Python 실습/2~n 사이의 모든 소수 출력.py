n = int(input("양의 정수 입력: "))
k = 0
for i in range(2, n+1):
    flag = 0
    for j in range(2, i):
        if i%j == 0:
            flag = 1
    if flag == 0:
        if k == 5:
            k = 0
            print("")
        print("%3d"%(i), end="")
        k += 1
              
