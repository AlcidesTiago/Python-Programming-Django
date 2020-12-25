# calculate simple interest
amt = int(input('enter amount:'))
rate = float(input('enter interest rate:'))
dura = int(input('enter duration(months):'))
simple_interest = float((amt * rate * dura) / 100)
print('Interest amount=', simple_interest)
total = amt + simple_interest
print('Total amount=', total)
