import random

def play_game():
    print("Welcome to the guessing game!")
    print("I have chosen a number between 1 and 10. Can you guess what it is?")

    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Initialize a variable to store the number of guesses the player has made
    guesses = 0

    # Initialize a flag to track whether the player has won the game
    win = False

    # Run the game loop until the player has guessed the correct number or run out of guesses
    while not win:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        guesses += 1

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations, you guessed the correct number!")
            print("You took {} guesses.".format(guesses))
            win = True
        # Check if the player has run out of guesses
        elif guesses >= 5:
            print("Sorry, you ran out of guesses. The correct number was {}.".format(secret_number))
            break
        # The guess must be incorrect
        else:
            # Check if the guess is too high
            if guess > secret_number:
                print("Your guess is too high. Try again.")
            # The guess must be too low
            else:
                print("Your guess is too low. Try again.")

    # Ask the player if they want to play again
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

play_game()
