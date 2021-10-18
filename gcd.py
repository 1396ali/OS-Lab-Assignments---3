#7

a = int(input('a: '))
b = int(input('b: '))

if a>b :
    smaller = b

else:
    smaller = a

for i in range(1 , smaller+1):
    if((a%i==0) and (b%i==0)):
        gcd=i

print('GCD is : ' , gcd)