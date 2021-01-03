import random

randomNo =  random.randint(1,100)
guess = 1
number = None

with open("highscore.txt","r") as f:
    high = f.read()
print(f"HighScore Is {high} Best Of Luck!!")

while(number != randomNo):
        
    number = int(input("Enter You Choice:- "))

    if (number == randomNo):
        print("Your Guess Is Correct And You Score High")
        print(f"Your Entered Correct number in {guess} guesses and it is {number}")

    elif(number < randomNo):
        print("You Entered Lowest Number")
        print("Please Enter Largest Number!!!")
 
    elif(number > randomNo):
        print("You Entered Largest Number")
        print("Please Enter Lowest Number ")
   
    else:
        print("Please Enter Nunber Between 1 to 100")

    guess += 1 

with open("highscore.txt","r") as f:
    high = int(f.read())

if(high > guess):
    with open("highscore.txt","w") as f:
        f.write(str(guess))
