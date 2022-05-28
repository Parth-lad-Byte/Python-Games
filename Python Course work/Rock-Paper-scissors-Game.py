import random  # imports the random module
import time

while True:
    print("~Welcome to Rock Paper Scissors Game~")
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock,paper,or scissors?: ").lower()
        print("Rock 🗿...")
        time.sleep(2)
        print("Paper 📄...")
        time.sleep(2)
        print("Scissors ✂...")
        time.sleep(2)
    if player == computer:

        print("Bot picked : " + computer)
        print("I pick: " + player)
        print("We tied!")
    elif player == "rock":
        if computer == "paper":
            print("Bot picked : " + computer)
            print("I pick: " + player)
            print("You lose!")
            if computer == "scissor":
                print("Bot picked : " + computer)
                print("I pick: " + player)
                print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Bot picked : " + computer)
            print("I pick: " + player)
            print("You lose!")
            if computer == "paper":
                print("Bot picked : " + computer)
                print("I pick: " + player)
                print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Bot picked : " + computer)
            print("I pick: " + player)
            print("You lose!")
            if computer == "rock":
                print("Bot picked : " + computer)
                print("I pick: " + player)
                print("You win!")


    play_again = input("Play Again? (Yes/No): ").lower()

    if play_again != 'yes':
        break
print("Bye!")
© 2022 GitHub, Inc.
Terms
Privacy
Security
