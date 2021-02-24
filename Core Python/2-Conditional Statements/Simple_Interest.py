# Simple Interest  Example

Amount = float(input('Enter the amount:'))
Rate = float(input('Enter your rate:'))
duration = int(input('Enter the duration'))

ts = (Amount * duration * Rate)/100

print('Simple Interest =', ts)