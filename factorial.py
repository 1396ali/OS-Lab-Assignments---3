#4

number = int(input('enter your number : '))

fa = i = 1

while fa < number:
    fa *= i
    i +=1

if number == fa:
    print('Yes')
else:
    print('No')
