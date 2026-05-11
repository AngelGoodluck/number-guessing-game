import random

#This will generate a number from 1 to 10
randomNumGenerated = random.randrange(1, 11)

#Here, we get the user's first guess
numEntered = int(input("Guess the number btw 1 and 10: "))

#It keeps looping as long as the guess is wrong
while numEntered != randomNumGenerated:
    # Giving hints inside the loop based on the current wrong guess
    if numEntered > randomNumGenerated:
        print("The number you guessed is too high! The random number is smaller.")
    else:
        print("The number you guessed is too low! The random number is larger.")
        
    # Asking for a NEW guess and update the variable so the loop can eventually end
    numEntered = int(input("Try again: "))

# If the loop ends, it means numEntered == randomNumGenerated
print("Yes, that's right! You won!")
