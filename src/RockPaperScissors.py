# Rock Paper and Scissors game
import random
from tkinter import *

root = Tk()
root.title("Rock & Paper & Scissors")
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(500, 600))
# creat label
gameLabel1 = Label(root, text="Welcome to Rock, Paper, Scissors.\nPlease pick your weapon", padx=50, fg="blue")
gameLabel1.pack()
pick = Label(root)  # for the destroy


# Click Start and now you can click on Paper Rock and Scissors
def Click():
    rockButton.pack(pady=20)
    paperButton.pack(pady=20)
    scissorsButton.pack(pady=20)
    if newButton["state"] == NORMAL:
        newButton["state"] = DISABLED
        rockButton["state"] = NORMAL
        paperButton["state"] = NORMAL
        scissorsButton["state"] = NORMAL


# button-start
photo = PhotoImage(file="assets/image/start.png")
photoing = photo.subsample(4, 4)
newButton = Button(root, image=photoing, command=Click, borderwidth=0)
newButton.pack(pady=20)


# A player chose a rock
def Rock():
    showButton()
    print("Rock- player")
    # pick1 = Label(root, text="Player - Rock", padx=50, fg="blue")
    # pick1.pack()
    choice = "Rock"
    computer = computer_choice()
    return game(choice, computer)


# Player Select Paper
def Paper():
    showButton()
    print("Paper- player")
    # pick1 = Label(root, text="Player - Paper", padx=50, fg="blue")
    # pick1.pack()
    computer = computer_choice()
    choice = "Paper"
    return game(choice, computer)


# Player Select Scissors
def Scissors():
    showButton()
    print("Scissors- player")
    computer = computer_choice()
    choice = "Scissors"
    return game(choice, computer)


# What is the status of the button. Is it possible to click on it or not?
def showButton():
    if rockButton['state'] == NORMAL:
        rockButton["state"] = DISABLED
    if paperButton['state'] == NORMAL:
        paperButton["state"] = DISABLED
    if scissorsButton['state'] == NORMAL:
        scissorsButton["state"] = DISABLED
    if paperButton['state'] == DISABLED:
        newButton["state"] = NORMAL


# Rock button
logo1 = PhotoImage(file=r"assets/image/Rock.png")
photoing1 = logo1.subsample(3, 3)
rockButton = Button(root, image=photoing1, command=Rock, borderwidth=0)

# Paper button
logo2 = PhotoImage(file=r"assets/image/Paper.png")
photoing2 = logo2.subsample(3, 3)
paperButton = Button(root, image=photoing2, command=Paper, borderwidth=0)

# Scissors button
logo3 = PhotoImage(file=r"assets/image/Scissors.png")
photoing3 = logo3.subsample(3, 3)
scissorsButton = Button(root, image=photoing3, command=Scissors, borderwidth=0)


# Random selection of the computer
def computer_choice():
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
    global pick
    pick.destroy()  # Modify the text without adding lines
    pick = Label(root, text="", padx=50, fg="red")
    pick.pack()
    player = player
    computer = computer
    if computer == player:  # Scissors Scissors: Rock Rock: Paper Paper
        print("Same selection")
        return pick.config(text="Same choices, try again", fg="red", font='Helvetica 15 bold')

    elif computer == "Rock" and player == "Scissors":
        print("Computer is the winner!")
        return pick.config(text="the computer select Rock\n\nyou chose Scissors \n\nCOMPUTER is the WINNER!!!", fg="green", font='Helvetica 15 bold')

    elif computer == "Rock" and player == "Paper":
        print("You are the winner!")
        return pick.config(text="computer select Rock\n\nyou chose Paper\n\nYOU are the WINNER!!!", fg="blue", font='Helvetica 15 bold')

    elif computer == "Paper" and player == "Scissors":
        print("You are the winner!")
        return pick.config(text="the computer select Paper\n\nyou chose Scissors\n\nYOU are the WINNER!!!", fg="blue", font='Helvetica 15 bold')

    elif computer == "Paper" and player == "Rock":
        print("Computer is the winner!")
        return pick.config(text="the computer select Paper\n\nyou chose a Rock\n\nCOMPUTER is the WINNER!!!", fg="green", font='Helvetica 15 bold')

    elif computer == "Scissors" and player == "Paper":
        print("Computer is the winner!")
        return pick.config(text="the computer selectScissors\n\nyou chose Paper\n\nCOMPUTER is the WINNER!!!", fg="green", font='Helvetica 15 bold')

    elif computer == "Scissors" and player == "Rock":
        print("You are the winner!")
        return pick.config(text="the computer select Scissors\n\nyou chose a Rock\n\nYOU are the WINNER!!!", fg="blue", font='Helvetica 15 bold')


root.mainloop()  # start over
