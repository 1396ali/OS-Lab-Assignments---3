#2
import random

random_numbers = []

inp = int(input('How much integer you want : '))

i = 0
    
while i<inp:
    x = random.randint(1 , inp)
    if not (x in random_numbers):
        random_numbers.append(x)
        i += 1

print(random_numbers)