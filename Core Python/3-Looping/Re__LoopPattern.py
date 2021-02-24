# ex7 Pattern
# n1 = 1
# n = 6
# for i in range(n1, n):
#     for g in range(1, i):
#         print("", end=" ")
#     for j in range(n1, 7-i):
#         print("*", end="")
#     print(" \t")

# ex8 Pattern
# col = 1
# rows = 4
# for i in range(col, rows):
#     for g in range(1, i):
#         print("", end="")
#     for j in range(rows, 4 + i):
#         print(i*i, end=" ")
#     print("\t")

# ex9 Pattern
# col = 1
# rows = 6
# for i in range(col, rows):
#     for g in range(1, i):
#         print("", end="")
#     for j in range(col, 7 - i):
#         print(i, end="")
#     print(" \t")

# ex11 Pattern
col = 1
rows = 6
for i in range(1, 6):
    for j in range(col, i + 1):
        print(i, end=" ")
    print("\t")