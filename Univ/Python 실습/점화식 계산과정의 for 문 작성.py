s = an = 1
n = int(input("n: "))
for i in range(2, n+1):
    an = an + i
    s = s + an
print("%d항까지의 합 = %d"%(n,s))
