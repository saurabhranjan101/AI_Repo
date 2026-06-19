'''
The game() function in a program lets a user play a game and returns the score as an integer. 
You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
'''
import random
def game():
    print("You are playing a game.")
    score = random.randint(1, 62)
    #fetch the high score
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore = int(hiscore)  #convert this into integer and store in hiscore. Type casting
        else:
            hiscore = 0
    print(f"Your score - {score}")
    if(score>hiscore):
        #write this high score to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score)) ##type casting
    return score
game()