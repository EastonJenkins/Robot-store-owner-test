#robot barista
#function for checking valid name
def checkName(name):
    allowedNames = ['easton', 'phillip', 'caleb', 'ankit', 'ashton', 'justin']
    allowedResponses = ['yes', 'yeah', 'yea', 'sure', 'y', 'ok']

    if name not in allowedNames:
        evilStatus = input('Are you a bad person?\n')
        age = int(input('Tell me, how old are you?\n'))
        if evilStatus.lower() in allowedResponses and age <= 16:

            print('Your not welcome here ' + name + ' get out of here.\n' )
            exit()
        else:
            print('Oh nice continue\n')
    else:
        print('Hello ' + name + ', welcome in\n')

def orderFood(name):
    menu = 'Milk, Water, Coffee'
    print(name + ', what do you want?\nToday we have ' + menu)
    order = input()
    match order.lower():
        case "milk":
            price = 13
        case "water":
            price = 15
        case "coffee":
            price = 12
        case _:
            print("Sorry, we don't have " + order)
            return

    quant = input('How many of this iteam would you like?\n')

    total = price * int(quant)

    print('Great, your total will be $' + str(total)) 

    print('Sounds good ' + name + ', your '+ quant + " " + order + " will be out in a sec")


print('Helllo, welcome to the shop.\n\n')
name = input('What is your name?')
checkName(name.lower())
orderFood(name)





