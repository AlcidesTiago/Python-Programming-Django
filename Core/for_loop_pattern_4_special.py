c = 0
for i in range(1, 4):
    for j in range(0, 3 * i):
        print(i, end=" ")
        c = c + 1
        if c % 3 == 0:
            print("")