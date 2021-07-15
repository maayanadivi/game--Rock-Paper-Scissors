# Rock Paper and Scissors game
import random
from tkinter import *

root = Tk()
root.title("Rock & Paper & Scissors")
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(500, 500))
# creat label
gameLabel1 = Label(root, text="Welcome to Rock, Paper, Scissors.\nPlease pick your weapon", padx=50, fg="blue")
gameLabel1.pack()


def Click():
    pass


# button-start
photo = PhotoImage(file="assets/image/start.png")
photoimage = photo.subsample(3, 3)
newButton = Button(root, image=photoimage, command=Click, borderwidth=0)
newButton.pack(pady=20)


def Rock():
    print("Rock- player")
    choice = "Rock"
    computer = computer_choice()
    return game(choice, computer)


def Paper():
    print("Paper- player")
    computer = computer_choice()
    choice = "Paper"
    return game(choice, computer)


def Scissors():
    print("Scissors- player")
    computer = computer_choice()
    choice = "Scissors"
    return game(choice, computer)


logo1 = PhotoImage(file=r"assets/image/Rock.png")
photoimage1 = logo1.subsample(3, 3)
rockButton = Button(root, image=photoimage1, command=Rock, borderwidth=0)
rockButton.pack(pady=20)

logo2 = PhotoImage(file=r"assets/image/Paper.png")
photoimage2 = logo2.subsample(3, 3)
paperButton = Button(root, image=photoimage2, command=Paper, borderwidth=0)
paperButton.pack(pady=20)

logo3 = PhotoImage(file=r"assets/image/Scissors.png")
photoimage3 = logo3.subsample(3, 3)
scissorsButton = Button(root, image=photoimage3, command=Scissors, borderwidth=0)
scissorsButton.pack(pady=20)











# Random selection of the computer
def computer_choice():
    option = ["Rock", "Paper", "Scissors"]
    x = random.randint(0, 2)
    if x == 0:
        print("rock- computer")
        return "Rock"
    elif x == 1:
        print("paper- computer")
        return "Paper"
    else:
        print("scissors- computer")
        return "Scissors"


def game(player, computer):
    player = player
    computer = computer
    if computer == player:
        return print("Same selection")
    elif computer == "Rock" and player == "Scissors":
        return print("Computer is the winner!")
    elif computer == "Rock" and player == "Paper":
        return print("You are the winner!")
    elif computer == "Paper" and player == "Scissors":
        return print("You are the winner!")
    elif computer == "Paper" and player == "Rock":
        return print("Computer is the winner!")
    elif computer == "Scissors" and player == "Paper":
        return print("Computer is the winner!")
    elif computer == "Scissors" and player == "Rock":
        return print("You are the winner!")


root.mainloop()
