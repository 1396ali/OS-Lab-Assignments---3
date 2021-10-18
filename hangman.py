#1
import random

word_dictianory_1 = ['apple' , 'peach' , 'banana' , 'watermeloon' ]

word_dictianory_2 = ['cat' , 'dog' , 'horse' , 'monkey' , 'fly' ]

kind=int(input('1(fruite) or 2(animal) :'))

if kind==1:
    word = random.choice(word_dictianory_1)
elif kind==2:
    word = random.choice(word_dictianory_2)


health = len(word)

print('Your health : ',health)


true_character = []

while True:

    winner = True

    for char in word:
        
        if char in true_character:
            print(char , end='')
        else:
            print('-' , end='')
            winner = False

    if winner:
        print ('\n YOU WIN - whith health : ' , health)
        break
    
    
    user_character = input('\n Inter a character : ')

    if user_character in word:
        true_character.append(user_character)
        
        print('OK')
    else:
        health -= 1
        print('NO - health :' , health)

   
    if health == 0:
        print ('GAME OVER!')
        break