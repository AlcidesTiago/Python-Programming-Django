a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))
d = int(input("Enter D: "))
e = int(input("Enter E: "))

total = a + b + c + d + e
percentage = ((total) / 5)
print (percentage)
if percentage < 35:
    print("sorry..you have not cleared this exam")
elif percentage > 35 or percentage < 60:
    print("second")
elif percentage > 60 or percentage < 70:
    print("first")
elif percentage > 70 or percentage < 100:
    print("distinction")

