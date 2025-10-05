import random

while True:
    secret_number = random.randint(1, 20)
    guesses = 0  # counter for number of tries

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        guesses += 1

        match guess:
            case guess_storage if guess_storage == secret_number:
                print(f" Congratulations, you guessed it in {guesses} tries!")
                break
            case guess_storage if guess_storage > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case guess_storage if guess_storage < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

    # Ask if they want to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break