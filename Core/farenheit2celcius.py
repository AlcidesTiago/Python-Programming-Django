def far2cel():
    temp = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (temp - 32) * 5 / 9
    print('Temperature in Celsius is {}'.format(celsius))


def cel2far():
    temp = float(input("Enter the temperature in Celsius: "))
    far = (temp * 9 / 5) + 32
    print('Temperature in Fahrenheit is {}'.format(far))


print("Choose between Celsius to Fahrenheit or Fahrenheit to Celsius: ")
print('A. Celsius to Fahrenheit')
print('B. Fahrenheit to Celsius')

inp = input()

if inp == 'A':
    cel2far()
elif inp == 'B':
    far2cel()
