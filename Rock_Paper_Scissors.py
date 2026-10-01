import random
user_score = 0
computer_score = 0
while True:
    print("---------Rock Paper Scissors Game---------")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    choices = ["Rock", "Paper", "Scissors"]
    try:
        user = int(input("Choose one of the following options: "))
    except ValueError:
        print("Only digits are allowed. Try again.")
        continue        
    if user == 1:
        user = "Rock"
    elif user == 2:
        user = "Paper"
    elif user == 3:
        user = "Scissors"    
    elif user == 4:
        print("Goodbye!")
        break
    else:
        print("Wrong input. Try again.")
        continue 

    print("You chose: ", user)
    computer = random.choice(choices)
    print("Computer chooses: ", computer)

    if user == computer:
        print("Result: Draw ✅")
    elif user == "Rock" and computer == "Scissors":
        print("Result: You win!")
        user_score += 1

    elif user == "Scissors" and computer == "Paper":
        print("Result: You win!")
        user_score += 1    

    elif user == "Paper" and computer == "Rock":
        print("Result: You win!")
        user_score += 1    
    else:
        print("You lose! Computer wins.")
        computer_score += 1
    print("Your score: ",user_score)
    print("Computer's score: ",computer_score)    