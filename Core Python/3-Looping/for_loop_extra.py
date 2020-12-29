for i in range(1, 6):
    for k in range(1, 6 - i):
        print(' ', end=' ')
    for j in range(0, i):
        print(' * ', end=' ')
    print('')
for a in range(5, 0, -1):
    if a == 5:
        pass
    else:
        for b in range(a, 5):
            print(' ', end=' ')
        for c in range(0, a):
            print(' * ', end=' ')
    print('')