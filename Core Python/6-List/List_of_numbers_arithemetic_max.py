# List_of_numbers
# numlist = [10, 2, 5, 7, 1]
# for i in numlist:
#     print(i, end= ', ')
# box = 0
# for i in numlist:
#     if i% 2 !=0:
#         box = box + 1
# print(box)

# Arithmetic
# numlist = [10, 2, 5, 7, 1]
# box = 0
# mul = 1
# sub = 2
# for i in numlist:
#     box = box + i
#     mul = mul * i
#     sub = sub - i
# print('Sum = ', box)
# print('Mul = ', mul)
# print('Sub = ', sub)

# Max
numlist = [10, 2, 5, 7, 1]
max = numlist[0]
for i in numlist:
    if i < max:
        max = i
print(max)