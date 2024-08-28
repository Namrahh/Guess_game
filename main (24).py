import random

def guess_checker(guess, answer, lives):
    """it will check the user's guess against the answer and return the updated lives."""
    if guess > answer:
        print("Too high.")
        return lives - 1
    elif guess < answer:
        print("Too low.")
        return lives - 1
    else:
        print("You got it right!")
        return 0 #the guess was correct, by returning 0, the game can detect that the user has guessed correctly and should end the game.

def set_difficulty():
    """Set the difficulty level and return the number of lives."""
    level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Invalid input. Setting difficulty to 'easy' by default.")
        return 10

def play_game():
    """Main function to play the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


    answer = random.randint(1, 100)
    # For cheating purpose
    # print(f"Pssst, the correct answer is {answer}")

    lives = set_difficulty()
    guess = 0

    while guess != answer and lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess: "))
            lives = guess_checker(guess, answer, lives)
        except ValueError:
            print("Invalid input. Please enter an integer.")

        if lives == 0 and guess != answer:
            print(f"You've run out of guesses. The correct answer was {answer}.")

def play_again(): 
    user_input = input("Do you want to play again? type yes or no: \n".lower())
    if user_input == "yes":
        play_game()
    else:
        "Thank you for playing the Number Guessing Game!"

def main():
    play_game()

main()
play_again()

# restart the game by asking for input