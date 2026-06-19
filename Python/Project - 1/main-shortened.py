import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
else: 
    '''
    if(computer == -1 and you == 1): (compuer - you) = -2
        print("You won!")
    elif(computer == -1 and you == 0): (compuer - you) = -1
        print("You loose!")
    elif(computer == 1 and you == -1): (compuer - you) = 2
        print("You loose!")
    elif(computer == 1 and you == 0): (compuer - you) = 1
        print("You won!")
    elif(computer == 0 and you == 1): (compuer - you) = -1
        print("You loose!")
    else:
        print("Something went wrong!")
        '''
    if((computer-you) ==-1 or (computer-you) == 2):
        print("you loose")
    else:
        print("you win")