#Blackjack Casion
# (V 2.0.0)
# By: James Denbow

# TABLE OF CONTENTS ##########################################################################################################################
#
#    LINE 00 - IMPORTS
#
#    LINE 00 - OBJECTS
#       + LINE 00 - Player [Represents User, CPUs & Dealer to manage hand, money, etc.]
#       + LINE 00 - Deck [Allows for deck management including dealing & shuffling]
#
#    LINE 00 - BLACKJACK ROUND MANAGER
#
#    LINE 00 - GAME MANAGEMENT & DISPLAY FUNCTIONS
#       + LINE 00 - game_manager() [Tracks player money, allowing play till money is out]
#       + LINE 00 - initialize_game() [Creates the ordered list of players when a new game starts]
#       + LINE 00 - menu2() [Second page of new game menu, allows position and starting money selection]
#       + LINE 00 - menu() [First page of new game menu, allows for CPU status selection and naming of players]
#       + LINE 00 - splash_screen() [Displays Splash Screen on launch]
#
#    LINE 00 - MAIN FUNCTION
#
##############################################################################################################################################

# IMPORTS ####################################################################################################################################
from tkinter import *
import random
##############################################################################################################################################

# OBJECTS ####################################################################################################################################
class Player:
    def __init__(self, name, money, status):
        self.status = status
        self.name = name
        self.money = money
        self.current_hand  = []
        self.current_bet = 0

class Deck:
    def __init__(self):
        self.standard_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]

    def shuffle(self):
        random.shuffle(self.standard_deck)

    def deal(self, current_player):
        current_player.current_hand.append(self.standard_deck[0])
        del self.standard_deck[0]
##############################################################################################################################################














def play_game():
    #Player action button
    actionFrame = Frame(window, width=230, height=215)
    actionFrame.place(anchor=SW, relx=0.01, rely=0.95)
    hitButton = Button(actionFrame, text="HIT", bg='green', fg='white', font="none 20 bold", width=13).grid(row=0)
    stayButton = Button(actionFrame, text="STAY", bg='red', fg='white', font="none 20 bold", width=13).grid(row=1)
    doubleButton = Button(actionFrame, text="DOUBLE", bg='blue', fg='white', font="none 20 bold", width=13).grid(row=2)
    splitButton = Button(actionFrame, text="SPLIT", bg='purple', fg='white', font="none 20 bold", width=13).grid(row=3)

    #Player statistics area
    statisticFrame = Frame(window, width=375, height= 710, bg="#1b1b1b")
    statisticFrame.place(anchor=SE, relx=1, rely=0.96)
    Label(statisticFrame, text=playername, bg="#1b1b1b", fg="white", font="none 23 bold", width=20).grid(row=0)
    Label(statisticFrame, text=currentbet, bg="#1b1b1b", fg="white", font="none 23 bold", width=20).grid(row=1)
    Label(statisticFrame, text=" On Hit -", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=2, pady=(100,0))
    Label(statisticFrame, text="    Win: ", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=3)
    Label(statisticFrame, text="    Push: ", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=4)
    Label(statisticFrame, text="    Bust: ", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=5)
    Label(statisticFrame, text=" On Stay -", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=6, pady=(30,0))
    Label(statisticFrame, text="    Win: ", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=7)
    Label(statisticFrame, text="    Push: ", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=8)
    Label(statisticFrame, text=" Reccomend: ", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=9, pady=(30,0))
    exitButtonsFrame = Frame(statisticFrame, bg="#1b1b1b")
    exitButtonsFrame.grid(row=10, pady=(100,10))
    menuButton = Button(exitButtonsFrame, text="M", font="none 23 bold").grid(row=0, column=1, padx=(10,10))
    exitButton = Button(exitButtonsFrame, text="X", font="none 23 bold").grid(row=0, column=2, padx=(10,10))

    #Current money area
    moneyFrame = Frame(window)
    moneyFrame.place(anchor=NE, relx=0.99, rely=0)
    Label(moneyFrame, text=currentmoney, bg="#43ac35", fg="white", font="none 23 bold").grid(row=0)





# BLACKJACK ROUND MANAGER ####################################################################################################################

    #Begins and manages the rounds of blackjack, makes calls to the game logic
    def blackjack_round(playerlist):
        temp############################################################################

##############################################################################################################################################

# GAME MANAGEMENT & DISPLAY FUNCTIONS ########################################################################################################

#The main game function, controls the flow of the game
def game_manager(playerlist, playerMoneyTracker):
    #Allows the player to continue playing rounds of blackjack until player is out of money
    while playerMoneyTracker > 0:
        playerMoneyTracker = blackjack_round(playerlist)

    #After the game is over return the player to the menu
    menu()


#Initializes the playerlist for the upcoming game
def initialize_game(playerPosition, moneyStart, playerName, cpu1Name, cpu1Status, cpu2Name, cpu2Status, cpu3Name, cpu3Status, cpu4Name, cpu4Status):
    playerlist = []

    #If a CPU player is in the game create a Player Object for them
    tempPlayerList = []
    if cpu1Status != 'none':
        tempPlayer = Player(cpu1Name, moneyStart, cpu1Status)
        tempPlayerList.append(tempPlayer)
    if cpu2Status != 'none':
        tempPlayer = Player(cpu2Name, moneyStart, cpu2Status)
        tempPlayerList.append(tempPlayer)
    if cpu3Status != 'none':
        tempPlayer = Player(cpu3Name, moneyStart, cpu3Status)
        tempPlayerList.append(tempPlayer)
    if cpu4Status != 'none':
        tempPlayer = Player(cpu4Name, moneyStart, cpu4Status)
        tempPlayerList.append(tempPlayer)

    #Create a Player Object for the User controlled Player
    user = Player(playerName, moneyStart, 'user')

    #Creates the playerlist in the order decided by the player during the menu screen
    if playerPosition == 1:
        playerlist.append(user)
        for i in tempPlayerList:
            playerlist.append(i)
    else:
        i = 1
        while i < playerPosition:
            temp = tempPlayerList.pop(0)
            playerlist.append(temp)
            i += 1
        playerlist.append(user)
        for i in tempPlayerList:
            playerlist.append(i)

    #Calls the game manager function, passing along the playerlist
    game_manager(playerlist, moneyStart)


#Second page of new game menu
def menu2(playerName, cpu1Name, cpu1Status, cpu2Name, cpu2Status, cpu3Name, cpu3Status, cpu4Name, cpu4Status):
    #Determines the total player count based on how many CPUs are set
    player_counter = 1
    if cpu1Status != 'none':
        player_counter += 1
    if cpu2Status != 'none':
        player_counter += 1
    if cpu3Status != 'none':
        player_counter += 1
    if cpu4Status != 'none':
        player_counter += 1

    menuFrame = Frame(window, bg="#43ac35").place(x=0, y=0, relwidth=1, relheight=1)
    #Main Menu label
    Label(window, text="Blackjack Casino Menu", bg="#43ac35", fg="white", font="none 30 bold").grid(row=0, pady=(0,100))

    #If there are CPUs allow the player to decide their position on the table
    if player_counter > 1:
        Label(window, text="Player Position: ", bg="#43ac35", fg="white", font="none 23 bold").grid(row=1, column=0, sticky='e')
        playerPosition = Scale(window, from_=1, to=player_counter, orient="horizontal", tickinterval=1, length=500)
        playerPosition.set(1)
        playerPosition.grid(row=1, column=1)
        Label(window, text=' ', bg="#43ac35", font="none 23 bold").grid(row=2)

    #Allow the player to decide the starting amount of money each player gets
    Label(window, text="Starting Money: ", bg="#43ac35", fg="white", font="none 23 bold").grid(row=3, column=0, sticky='e')
    moneyStart = Scale(window, from_=100, to=10000, orient="horizontal", tickinterval=1000, length=500)
    moneyStart.set(1000)
    moneyStart.grid(row=3, column=1)

    #Checks if any player names are blank and if so provides a default name
    if playerName == '':
        playerName = 'User'
    if cpu1Name == '':
        cpu1Name = 'CPU Player 1'
    if cpu2Name == '':
        cpu2Name = 'CPU Player 2'
    if cpu3Name == '':
        cpu3Name = 'CPU Player 3'
    if cpu4Name == '':
        cpu4Name = 'CPU Player 4'

    #Start game button that begins the initialize_game function
    startButton = Button(window, text="Start", font="none 17 bold", command=lambda: initialize_game(playerPosition.get(), moneyStart.get(), playerName, cpu1Name, cpu1Status, cpu2Name, cpu2Status, cpu3Name, cpu3Status, cpu4Name, cpu4Status)).grid(row=4, column=2, pady=(50, 0))


#Menu Page 1, menu for new game
def menu():
    #List of CPU statuses
    status = ["none", "beginner", "normal", "expert"]

    menuFrame = Frame(window, bg="#43ac35").place(x=0, y=0, relwidth=1, relheight=1)
    #Main Menu label
    Label(window, text="Blackjack Casino Menu", bg="#43ac35", fg="white", font="none 30 bold").grid(row=0, pady=(0,100))

    #Gathers the desired name for player
    Label(window, text="Player Name: ", bg="#43ac35", fg="white", font="none 23 bold").grid(row=1, column=0, sticky='e')
    playerName = Entry(window, font="none 23")
    playerName.grid(row=1, column=1)

    Label(window, text=' ', bg="#43ac35", font="none 23 bold").grid(row=2)

    #Gathers the status and names for all CPU players
    Label(window, text="CPU Player Name: ", bg="#43ac35", fg="white", font="none 23 bold").grid(row=3, column=0, sticky='e')
    cpu1Name = Entry(window, font="none 23")
    cpu1Name.grid(row=3, column=1)
    cpu1Status = StringVar(window)
    cpu1Status.set(status[2])
    cpu1menu = OptionMenu(window, cpu1Status, *status)
    cpu1menu.config(font="none 15 bold")
    cpu1menu.grid(row=3, column=2, sticky='w')
    Label(window, text="CPU Player Name: ", bg="#43ac35", fg="white", font="none 23 bold").grid(row=4, column=0, sticky='e')
    cpu2Name = Entry(window, font="none 23")
    cpu2Name.grid(row=4, column=1)
    cpu2Status = StringVar(window)
    cpu2Status.set(status[2])
    cpu2menu = OptionMenu(window, cpu2Status, *status)
    cpu2menu.config(font="none 15 bold")
    cpu2menu.grid(row=4, column=2, sticky='w')
    Label(window, text="CPU Player Name: ", bg="#43ac35", fg="white", font="none 23 bold").grid(row=5, column=0, sticky='e')
    cpu3Name = Entry(window, font="none 23")
    cpu3Name.grid(row=5, column=1)
    cpu3Status = StringVar(window)
    cpu3Status.set(status[2])
    cpu3menu = OptionMenu(window, cpu3Status, *status)
    cpu3menu.config(font="none 15 bold")
    cpu3menu.grid(row=5, column=2, sticky='w')
    Label(window, text="CPU Player Name: ", bg="#43ac35", fg="white", font="none 23 bold").grid(row=6, column=0, sticky='e')
    cpu4Name = Entry(window, font="none 23")
    cpu4Name.grid(row=6, column=1)
    cpu4Status = StringVar(window)
    cpu4Status.set(status[2])
    cpu4menu = OptionMenu(window, cpu4Status, *status)
    cpu4menu.config(font="none 15 bold")
    cpu4menu.grid(row=6, column=2, sticky='w')

    #Button that triggers the second menu page
    nextButton = Button(window, text="Next", font="none 17 bold", command=lambda: menu2(playerName.get(), cpu1Name.get(), cpu1Status.get(), cpu2Name.get(), cpu2Status.get(), cpu3Name.get(), cpu3Status.get(), cpu4Name.get(), cpu4Status.get())).grid(row=7, column=2, pady=(50, 0))


#Displays Start New Game Button
def splash_screen():
    #Splash Screen button, when pressed it open menu for new game
    startButton = Button(window, text="Start New Game", font="none 23 bold", command=menu).place(relx=0.444, rely=0.7)

##############################################################################################################################################

# MAIN FUNCTION ##############################################################################################################################
window = Tk()
window.title("Blackjack Casino (V 1.0.0)")
window.configure(background="black")
window.geometry('1920x1080')

#Create background
background = PhotoImage(file="background.gif")
Label(window, image=background, bg="#43ac35").place(x=0, y=0, relwidth=1, relheight=1)

#Call Splash Screen start
splash_screen()

#run main loop
window.mainloop()
##############################################################################################################################################
