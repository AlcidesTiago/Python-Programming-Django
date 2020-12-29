# count number which are divisible by
count = 0
for x in range(7, 51):
    if x % 5 == 0:
        count = count + 1
print(count)
