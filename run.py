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

def hasWon(playerChoice, computerChoice):
    """
    Function to calculate game combinations to show who has won the game.
    """      
    if (playerChoice == "Water" and computerChoice == "Fire") or (playerChoice == "Fire" and computerChoice == "Earth") or (playerChoice == "Earth" and computerChoice == "Water"):
        print("YOU WON! :D")
        return "Player"
    elif (playerChoice == "Fire" and computerChoice == "Water") or (playerChoice == "Earth" and computerChoice == "Fire") or (playerChoice == "Water" and computerChoice == "Earth"):
        print("YOU LOST :(")
        return "Computer"
    elif (playerChoice == computerChoice):
        print("TIE!")

    

