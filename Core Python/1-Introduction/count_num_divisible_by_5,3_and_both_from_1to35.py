# count_num_divisible_by_5,3_and_both_from_1to35
a = 0
b = 0
c = 0
for num in range(1, 36):
    if (num % 5 == 0) and (num % 3 == 0):
        c = c + 1
    elif num % 5 == 0:
        a = a + 1
    elif num % 3 == 0:
        b = b + 1
print('divisible by 5:', a)
print('divisible by 3:', b)
print('divisible by 5 & 3:', c)