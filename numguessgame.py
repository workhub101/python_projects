import random
number=random.randint(1,101)
guess1=""
attemps=0
attempsleft=6

while guess1 != number and attemps<=5:
    guess1=int(input("please guess a number from 1-100"))
    if guess1==number:
        print("you guessed the number")
    else:
        attemps=attemps+1
        attempsleft=attempsleft-1
        if guess1>number:
            print("the number is smaller then your guess")
        elif guess1<number:
            print("the number is greater then your guess")

        print("try again")
        print(f"you have {attempsleft} attemps left")
        
        
        if attemps>5:
            print("you have lost all your attempts")
            print(f"the secrect number was {number}")
        
        

    

  
        