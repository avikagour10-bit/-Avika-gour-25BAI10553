import random

choices = ["rock", "paper", "scissor"]

while True:
    user = input("Enter rock, paper, or scissor: ").lower()
    
    if user not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
