import random
def game():
    print("You are playing a game..")
    score = random.randint(1,62)
    #fetch the hiscore
    with open("Hiscore.txt","r") as f:
        hiscore = f.read() #This return string
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score:{score}")
    if(score > hiscore):
        #write this hiscore in the file
        with open("Hiscore.txt","w") as f:
            f.write(str(score))
    return score
game()