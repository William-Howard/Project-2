import random

play = True

while play:
    
 print("I'm thinking of a number between 1 and 100...")
 number = random.randint(1, 100)
 count = 1
 guess = int(input("Please guess a number: "))

 while guess != number:
     count+=1
     if guess < number:
         print("You guessed too low")
         guess = int(input("Please guess a number: "))
     else:
         print("You guessed too high")
         guess = int(input("Please guess a number: "))

 print("Congratulations! you guessed the number in",count, "tries!")

 again=str(input("Do you want to play again (Y/N)?"))
 if again == "no":
     play = False






