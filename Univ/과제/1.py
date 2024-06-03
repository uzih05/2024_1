def find():
    k = 0
    n = 1
    while k <= 100 :
        print(n)
        k += n
        n += 2
    return n

result = find()
print("100을 초과하는 최소 n:", result)
