for i in range(0, 3):
    for j in range(0, 3):
        print("*", end=" ")
    print("")
print('')

for i in range(1, 4):
    for j in range(0, i):
        print("*", end=" ")
    print("")
print('')

for i in range(3, 0, -1):
    for k in range(i, 3):
        print('', end=' ')
    for j in range(0, i):
        print("*", end=" ")
    print("")
print('')

for i in range(3, 0, -1):
    for k in range(1, i - 1):
        print('', end='')
    for j in range(0, i):
        print("* ", end=" ")
    print("")
print('')

for i in range(4, 0, -1):
    for k in range(0, 4-i):
        print('', end='')
    for j in range(0, i):
        print("*", end=" ")
    print("")
print('')