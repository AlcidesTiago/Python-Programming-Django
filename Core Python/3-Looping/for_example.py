# 3x3 bullets
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(" * ", end=" ")
#     print('\n')


# 3x3 with column wise numbers
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(j, '\t',end="")
#     print('\n')


# 3x3 with row wise numbers
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i,'\t', end="")
#     print('\n')


# normal tree with bullets
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*\t', end="")
#     print('\n')


# normal tree with column wise numbers
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j,'\t', end="")
#     print('\n')


# inverted tree with bullets
# for i in range(1, 6):
#     # print whitespaces
#     for k in range(1, 6 - i):
#         print("\t", end="")
#     # print bullets
#     for j in range(1, i + 1):
#         print('*\t', end="")
#     print('\n')


# upside inverted tree with bullets
# for i in range(5, 0, -1):
#     # print whitespaces
#     for k in range(1, 6 - i):
#         print("\t", end="")
#     # print bullets
#     for j in range(1, i + 1):
#         print('*\t', end="")
#     print('\n')


# upside normal tree with bullets
# for i in range(5, 0, -1):
#     # print bullets
#     for j in range(1, i + 1):
#         print('*\t', end="")
#     print('\n')


# pyramid with bullets
# for i in range(1, 6):
#     # print whitespaces
#     for k in range(1, 6 - i):
#         print(" ", end=" ")
#     # print bullets
#     for j in range(1, i + 1):
#         print(' * ', end=" ")
#     print('')


# tree with square of number of elements of row number
# for i in range(1, 4):
#     for j in range(1, i + 1):
#         print(i * i, end=" ")
#     print("")


# upside tree with square of number of row number
# for i in range(3, 0, -1):
#     for k in range(1, 4-i):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         print(i*i, end=" ")
#     print(" ")


# upside tree  with row wise numbers decreasing
# for i in range(5, 0, -1):
#     for k in range(1, 6-i):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print(" ")
