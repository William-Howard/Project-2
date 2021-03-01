# Project 2

Project 2 was made a year ago during my first semester of college. This project is more fun than the calculator in project 1. It's actually a bit easier than
the calculator project, due to there being less math in it. I also did this on Python.


## More interesting things about Python

- Python was actually a hobby project...at first.
- It was named after the comedy troupe Monty Python.
- Tim Peters wrote a poem in the script. Type "import this", and a special poem will pop up. (do it in the IDLE)
- NASA, Facebook, Spotify, and Uber all use Python.
- Python does not use braces to delimit code

# What is the purpose of Project 2?

The purpose of Porject 2 was to make a fun little game for people to enjoy. It's not complex at all really, in fact, I almost got it all correct on my first try. The game
will ask for you to guess a number between 1 and 100. Depending on what you choose, the game will inform you if you go too high or low. Once you have guessed the correct 
number, the game will inform you that you've won and will ask if you want to play again.

# How did you make this?

**1.)** First step is to 'import random'. Like last time, it allows us to import the needed materials for this project.
(ex. import random)

**2.)** The second step is to type 'play = true', and after that, you need to type "while play:". This allows the user to go into an infinite loop if they hit the correct
keys. In order to do this, you must use keywords at the beginning and end of the code. 
(ex. play = true and while play:)

**3.)** In the second part of the code, a message is recommended. The message usually says "I'm thinking of a number between 1 and 100", but this can be changed to whatever one wants. 
(ex. ("I'm thinking of a number between 1 and 100..."))

**4.)** After this, we will then type in a special command called 'random.randint' that allows us to choose numbers inbetween 1 and 100. This part also includes a counter that will help keep track of the guesses within the game, which is usually typed in as 'count = 0'. This counter is right above an input command that allows the user to put in their guess. 
(ex. random.randint, count = 0, and guess = int(input)

**5.)** Once the first main chunk of code is complete, we shall move on to the more complex second phase. In this phase we will allow the user to count the amount of guesses 
that they have inputted. This is accomplished by typing 'while guess != number: count +=1'. After that, the typed number will be compared to the actual number, allowing the code to discern wether or not it is too low or high. This is accomplished by typing in 'if guess < number: print("you guessed too low")'.
(ex. while guess != number:, count +=1, if guess < number:, print("you guessed too low"))

**6.)** The third phase is pretty similiar to the second, except that it needs the command 'else:'. The 'else' command allows the code to go into the third phase, creating a very similar line of code. Although instead of there being the line ("you guessed too low"), it becomes ("you guessed too high"). This is where the project begins to wrap up nice and pretty. 
(ex. else:, ("you guessed too low"), ("you guessed too high"))

**7.)** If the user has guessed correctly, a message saying '("Congratulations! You guessed the number in",count, "tries!") will pop up on the screen. Due to the counting of past guesses, the 'count' command allows the user to see how many times they guessed. 
(ex. ("Congratulations! You guessed the number in",count, "tries!"))

**8.)** The final part of the code includes the option of playing the game again. This is accomplished by asking ("Do you want to play again (Y/N)?). It's recommended that you include the input command before the question itself. If the player answers "no" the game will immediately end. This is allowed if the line says 'if again == "no":'. The final part of this code is to simply finish the loop stated in the first step. You accomplish this by typing 'play = false', which is essentially the opposite of the starting of the loop.
(ex. ("Do you want to play again (Y/N)?), 'play = false', and if again == "no":)

# Finished product and outputs

**Product**:

![project 2 code](https://user-images.githubusercontent.com/79774762/109440988-90515900-79f9-11eb-85d9-6c21c185db2d.png)

**Output**:

![Project 2](https://user-images.githubusercontent.com/79774762/109441075-dc040280-79f9-11eb-9f03-3cc890d25d50.png)


# Notes

- This is sadly not as malleable.
- It was satisfying to see it work.
- Both pictures are included in the files.
- Try to get a nice score!
- Have a nice day! :D


 
