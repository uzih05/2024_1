#for i in range(2, 10, 1):
#   for k in range(1, 10 ,1):
#       print("%d x %d = %2d"%(i,k,i*k))
#       print("")

for i in range(1, 10):
    for j in range(2, 10):
        print("%d x %d = %2d"%(j,i,j*i), end="\t")
    print("\n", end="")
