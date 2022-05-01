import random

print("-------------------------------------------------------------------")
print("Welcome to Water Earth Fire!")
print("A rock, paper, scissors type game based on Avatar The Last Airbender.")
print("--------------------------------------------------------------------")
print("HOW TO PLAY:")
print("Can you use your bending abilities to defeat your opponent?")
print("Water Beats Fire")
print("Fire Beats Earth")
print("Earth Beats Water")
print("Good Luck :D")

playerScore = 0
computerScore = 0

gameChoices = ["Water", "Fire", "Earth"]


while True:
    playerChoice = input("Enter Water / Fire / Earth or S to stop the game: ")

    if playerChoice == "s":
        break
    if playerChoice not in gameChoices:
        print("Invalid Input. Try Again")
        continue

    computerChoice = random.choice(gameChoices)
    print("Computer choice: ", computerChoice)

    if playerChoice == "Water" and computerChoice == "Fire":
        print("Woo! you Won")
        playerScore += 1
    elif playerChoice == "Fire" and computerChoice == "Earth":
        print("Woo! you Won")
        playerScore += 1
    elif playerChoice == "Earth" and computerChoice == "Water":
        print("Woo! you Won")
        playerScore += 1
    else:
        print("Sorry! You Lost :(")
        computerScore += 1


print("You Won", playerScore, "times.")
print("The Computer Won", computerScore, "times.")
print("GoodBye! Thanks for playing :D") 


