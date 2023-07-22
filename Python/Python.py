


input()
#robot barista
print('Helllo, welcome to the shop.\n\n')

name = input('What is your name?\n')
allowedNames = ['Easton', 'Phillip', 'Caleb', 'Ankit', 'Ashton', 'Justin']

if name not in allowedNames:
    evilStatus = input('Are you a bad person?\n')
    age = int(input('Tell me, how old are you?\n'))
    if evilStatus == "Yes" and age <= 16 or evilStatus == "yes" and age <= 16 or evilStatus == "sure" and age <= 16 or evilStatus == "Yeah" and age <= 16:

        print('Your not welcome here ' + name + ' get out of here.\n' )
        exit()
    else:
        print('Oh nice continue\n')
else:
    print('Hello ' + name + ', welcome in\n')




menu = 'Milk, Water, Coffee'

print(name + ', what do you want?\nToday we have ' + menu)

order = input()
if order == "Milk":
    price = 13
elif order == "Water":
    price = 15
elif order == "Coffe":
    price = 12
else:
    print("Sorry, we don't have " + order)
    price = 0

quant = input('How many of this iteam would you like?\n')

total = price * int(quant)

print('Great, your total will be $' + str(total)) 

print('Sounds good ' + name + ', your '+ quant + " " + order + " will be out in a sec")

