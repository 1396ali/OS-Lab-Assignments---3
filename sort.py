#6

inpu = []

inp = int(input('How much integer you want to enter : '))

i=1

while i <= inp:
    print('Enter your (' ,i, ') number : ' ,  end='')
    x = int(input())
    inpu.append(x)
    i +=1

print('Your input array is : ' , inpu)

flag=True

for ab in range(len(inpu)):
    
    for ba in range(ab+1 , len(inpu)):
    
        if inpu[ab]>inpu[ba]:
            flag=False
            
if flag==True:
    print('Yes')
else:
    print('No')    