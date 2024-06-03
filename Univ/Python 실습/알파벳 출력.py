for i in range(1, 27):
    for col in range(1, 40-i):
        print(" ", end="")
    for j in range(0, i):
        print("%c "%(ord('A')+j), end='')
    print("")
