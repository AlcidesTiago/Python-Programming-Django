# Conditional Statements
# 1) For loop
# 2) While loop
# Foreach loop - Associative Array(No Foreach in Python - We use for as Foreach)
# Range
# in



# 1) For loop
# x = range(1,10)
# for i in x:
#   print('{} Welcom'.format(i))

# Range

# 1) print odd no btwn 3 and 30
# 2) print the addition 1 to 5 = 15
# 3) print the mult from 1 to 5 = 120
# 4) count the numbers which are divisible by 5 from 7 to 50 = ?
# 5) print the sum btwn 3 to 25 which are not divible by 3=?


# # 1) print odd no btwn 3 and 30
# x = range(3, 31)
# for i in x:
#     if i % 2 != 0:
#         print(i, end=" ")
#     else:
#         pass


# # 2) print the addition 1 to 5 = 15
# add = 0
# for i in range(1, 6):
#     add = add + i
#     print('Total: {}'.format(add))

# 3) print the mult from 1 to 5 = 120
# mult = 1
# for i in range(1, 6):
#     mult = mult * i
#     print('Total: {}'.format(mult))

# 4) count the numbers which are divisible by 5 from 7 to 50 = ?
# count = 0
# for i in range(5, 51):
#     if i % 5 == 0:
#         count = count + 1
#         print('Count:{}'.format(count))
#     else:
#         pass


# # 5) print the sum btwn 3 to 25 which are not divible by 3 = ?
# sum = 1
# # for i in range(3, 26):
# #     if i % 3 == 0:
# #         sum = sum % 3
# #         print('sum:{}'.format(sum))
# #     else:
# #         pass

# 4) print count of numbers which are divisible by 5, 3 and (3 & 5 both) from 1 to 35
# t_3 = 0
# f_5 = 0
# f5_3t = 0
# for i in range(1, 36):
#     if (i % 5 == 0) and (i % 3 == 0):
#         f5_3t = f5_3t + 1
#     elif i % 5 == 0:
#         f_5 = f_5 + 1
#     elif i % 5 == 3:
#         f5_3t = f5_3t + 1
#
#     print('Three:{}'.format(t_3))
#     print('Five:{}.'.format(f_5))
#     print('Three & Five:{}.'.format(f5_3t))

