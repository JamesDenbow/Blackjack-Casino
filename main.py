#Blackjack Casion
# (V 2.2.1)
# By: James Denbow

# TABLE OF CONTENTS ##########################################################################################################################
#
#    LINE 39 - IMPORTS
#
#    LINE 47 - OBJECTS
#       + LINE 48 - Player [Represents User, CPUs & Dealer to manage hand, money, etc.]
#       + LINE 59 - Deck [Allows for deck management including dealing & shuffling]
#
#    LINE 114 - HELPER FUNCTIONS
#       + LINE 116 - chart_strategy_calc() [Calculates the appropriate move based on the Blackjack Chart Strategy, used in recommendations and expert CPUs]
#       + LINE 222 - end_round() [End of Round manager, determines win / loss and displays appropriate message, also handles updating of money]
#       + LINE 304 - exitFunc() [Function called when user hits the exit button, closes TK instance and shuts down all processes]
#       + LINE 310 - playerhit() [Function called when player asks for hit, calls deck to deal card and updates screen with appropriate card image]
#       + LINE 337 - cpu_beginner() [Function controls the game logic of Beginner level CPUs]
#       + LINE 346 - cpu_normal() [Function controls the game logic of Normal level CPUs]
#       + LINE 362 - cpu_expert() [Function controls the game logic of Expert level CPUs]
#       + LINE 370 - simulator() [Used to similuate possible outcomes after each move to calculate probable outcomes]
#       + LINE 445 - statistic_calc() [Calculates and displays all statistics to player, along with playername and current bet]
#       + LINE 517 - busted() [Called when a player reaches a score of 21 or higher to remove action buttons to prevent further action]
#       + LINE 524 - doubleDown() [Called when the player hits the double button, handles the double down case fully]
#
#    LINE 533 - BLACKJACK ROUND MANAGER
#
#    LINE 728 - GAME MANAGEMENT & DISPLAY FUNCTIONS
#       + LINE 730 - game_manager() [Tracks player money, allowing play till money is out]
#       + LINE 754 - initialize_game() [Creates the ordered list of players when a new game starts]
#       + LINE 795 - menu2() [Second page of new game menu, allows position and starting money selection]
#       + LINE 842 - menu() [First page of new game menu, allows for CPU status selection and naming of players]
#       + LINE 896 - splash_screen() [Displays Splash Screen on launch]
#
#    LINE 901 - MAIN FUNCTION
#
##############################################################################################################################################

# IMPORTS ####################################################################################################################################
from tkinter import *
import random
import time
import sys
import copy
##############################################################################################################################################

# OBJECTS ####################################################################################################################################
class Player:
    def __init__(self, name, money, status):
        self.status = status
        self.name = name
        self.money = money
        self.current_hand  = []
        self.current_hand_card = []
        self.current_bet = 0
        self.column_tracker = 0
        self.cpu_card_row = 0

class Deck:
    def __init__(self):
        self.standard_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
        self.decka = ['AC','AS','AH','AD']
        self.deck2 = ['2C','2S','2H','2D']
        self.deck3 = ['3C','3S','3H','3D']
        self.deck4 = ['4C','4S','4H','4D']
        self.deck5 = ['5C','5S','5H','5D']
        self.deck6 = ['6C','6S','6H','6D']
        self.deck7 = ['7C','7S','7H','7D']
        self.deck8 = ['8C','8S','8H','8D']
        self.deck9 = ['9C','9S','9H','9D']
        self.deck10 = ['10C','10S','10H','10D','JC','JS','JH','JD','QC','QS','QH','QD','KC','KS','KH','KD']

    def shuffle(self):
        random.shuffle(self.standard_deck)

    def deal(self, current_player):
        card = self.standard_deck[0]
        cardsuit = 'NA'
        del self.standard_deck[0]
        current_player.current_hand.append(card)
        if card == 2 and len(self.deck2) != 0:
            cardsuit = random.choice(self.deck2)
            self.deck2.remove(cardsuit)
        elif card == 3 and len(self.deck3) != 0:
            cardsuit = random.choice(self.deck3)
            self.deck3.remove(cardsuit)
        elif card == 4 and len(self.deck4) != 0:
            cardsuit = random.choice(self.deck4)
            self.deck4.remove(cardsuit)
        elif card == 5 and len(self.deck5) != 0:
            cardsuit = random.choice(self.deck5)
            self.deck5.remove(cardsuit)
        elif card == 6 and len(self.deck6) != 0:
            cardsuit = random.choice(self.deck6)
            self.deck6.remove(cardsuit)
        elif card == 7 and len(self.deck7) != 0:
            cardsuit = random.choice(self.deck7)
            self.deck7.remove(cardsuit)
        elif card == 8 and len(self.deck8) != 0:
            cardsuit = random.choice(self.deck8)
            self.deck8.remove(cardsuit)
        elif card == 9 and len(self.deck9) != 0:
            cardsuit = random.choice(self.deck9)
            self.deck9.remove(cardsuit)
        elif card == 10 and len(self.deck10) != 0:
            cardsuit = random.choice(self.deck10)
            self.deck10.remove(cardsuit)
        elif card == 11 or card == 1 and len(self.decka) != 0:
            cardsuit = random.choice(self.decka)
            self.decka.remove(cardsuit)
        current_player.current_hand_card.append(cardsuit)
##############################################################################################################################################

# HELPER FUNCTIONS ###########################################################################################################################
#Returns suggested move based on Chart Strategy
def chart_strategy_calc(current_player, upcard):
    #If double return 'd'
    #If hit return 'h'
    #If stay return 's'
    #If double / stay return 'z'
    #If split return 'p'

    #Check for split
    if current_player.status == 'user':
        if len(current_player.current_hand) == 2:
            if current_player.current_hand[0] == current_player.current_hand[1]:
                card_score = current_player.current_hand[0]
                if card_score != 10 and card_score != 4 and card_score != 5:
                    if card_score == 11 or card_score == 1:
                        return 'p'
                    elif card_score == 8:
                        return 'p'
                    elif card_score == 2 or card_score == 3:
                        if upcard == 4 or upcard == 5 or upcard == 6 or upcard == 7:
                            return 'p'
                        else:
                            return 'h'
                    elif card_score == 6:
                        if upcard == 3 or upcard == 4 or upcard == 5 or upcard == 6:
                            return 'p'
                        else:
                            return 'h'
                    elif card_score == 7:
                        if upcard != 1 and upcard < 8:
                            return 'p'
                        else:
                            return 'h'
                    elif card_score == 9:
                        if upcard == 7 or upcard == 10 or upcard == 11 or upcard == 1:
                            return 's'
                        else:
                            return 'p'
            elif current_player.current_hand[0] == 11 and current_player.current_hand[1] == 1:
                return 'p'
            elif current_player.current_hand[0] == 11 and current_player.current_hand[1] == 1:
                return 'p'

    #Check soft totals
    player_score = sum(current_player.current_hand)
    if 11 in current_player.current_hand:
        if player_score == 20:
            return 's'
        elif player_score == 19:
            if upcard == 6:
                return 'z'
            else:
                return 's'
        elif player_score == 18:
            if upcard > 8 or upcard == 1:
                return 'h'
            elif upcard == 7 or upcard == 8:
                return 's'
            else:
                return 'z'
        elif player_score == 17:
            if upcard == 3 or upcard == 4 or upcard == 5 or upcard == 6:
                return 'd'
            else:
                return 'h'
        elif player_score == 16 or player_score == 15:
            if upcard == 4 or upcard == 5 or upcard == 6:
                return 'd'
            else:
                return 'h'
        elif player_score == 14 or player_score == 13:
            if upcard == 5 or upcard == 6:
                return 'd'
            else:
                return 'h'

    #Check hard totals
    else:
        if player_score >= 17:
            return 's'
        elif player_score == 16 or player_score == 15 or player_score == 14 or player_score == 13:
            if upcard < 7 and upcard != 1:
                return 's'
            else:
                return 'h'
        elif player_score == 12:
            if upcard == 4 or upcard == 5 or upcard == 6:
                return 's'
            else:
                return 'h'
        elif player_score == 11:
            return 'd'
        elif player_score == 10:
            if upcard > 9 or upcard == 1:
                return 'h'
            else:
                return 'd'
        elif player_score == 9:
            if upcard == 3 or upcard == 4 or upcard == 5 or upcard == 6:
                return 'd'
            else:
                return 'h'
        elif player_score <= 8:
            return 'h'


#Function ends round and displays results
def end_round(dealer, playerlist, round_deck):
    dealer_score = sum(dealer.current_hand)
    dealer_length = len(dealer.current_hand)
    for i in playerlist:
        player_score = sum(i.current_hand)
        player_length = len(i.current_hand)

        if dealer_score == 21 and dealer_score == player_score:
            if dealer_length == 2 and player_length == 2:
                i.money += i.current_bet
            elif dealer_length == 2:
                i.money = i.money
            elif player_length == 2:
                i.money += int(2.5 * i.current_bet)
            else:
                i.money += i.current_bet
        elif dealer_score == 21 and dealer_length == 2:
            i.money = i.money
        elif player_score == 21 and player_length == 2:
            i.money += int(2.5 * i.current_bet)
        elif dealer_score > 21 and player_score <= 21:
            i.money += int(2 * i.current_bet)
        elif player_score > 21:
            i.money = i.money
        elif dealer_score == player_score:
            i.money += i.current_bet
        elif player_score > dealer_score:
            i.money += int(2 * i.current_bet)
        elif player_score < dealer_score:
            i.money = i.money

    condition = 'ERROR'
    index = 0
    user_index = 0
    for i in playerlist:
        if i.status == 'user':
            user_index = index
        index += 1

    player_score = sum(playerlist[user_index].current_hand)
    player_length = len(playerlist[user_index].current_hand)

    if dealer_score == 21 and dealer_score == player_score:
        if dealer_length == 2 and player_length == 2:
            condition = 'PUSH'
        elif dealer_length == 2:
            condition = 'LOSS - DEALER BLACKJACK'
        elif player_length == 2:
            condtion = 'WIN - BLACKJACK'
        else:
            condition = 'PUSH'
    elif dealer_score == 21 and dealer_length == 2:
        condition = 'LOSS - DEALER BLACKJACK'
    elif player_score == 21 and player_length == 2:
        condition = 'WIN - BLACKJACK'
    elif dealer_score > 21 and player_score <= 21:
        condition = 'WIN - DEALER BUST'
    elif player_score > 21:
        condition = 'LOSS - BUST'
    elif dealer_score == player_score:
        condition = 'PUSH'
    elif player_score > dealer_score:
        condition = 'WIN'
    elif player_score < dealer_score:
        condition = 'LOSS'

    player_money = playerlist[user_index].money

    #Delete all objects
    temp_playerlist = []
    del round_deck
    del dealer
    for i in playerlist:
        name = i.name
        status = i.status
        money = i.money
        temp_playerlist.append(Player(name,money,status))
    playerlist.clear()

    return condition, player_money, temp_playerlist


def exitFunc():
    window.destroy()
    _thread.interrupt_main()
    os._exit


def playerhit(round_deck, downcard, playerlist, index_player, currentplayer, frame, upcard):
    round_deck.deal(currentplayer)
    if currentplayer.name == 'dealer':
        cardname = "img/" + currentplayer.current_hand_card[-1] + ".gif"
        cardDealer = PhotoImage(file=cardname)
        cardLabelDealer = Label(frame, image=cardDealer, bg="#43ac35")
        cardLabelDealer.image = cardDealer
        cardLabelDealer.grid(row=0, column=currentplayer.column_tracker)
    elif currentplayer.status != 'user':
        cardname = "img/" + currentplayer.current_hand_card[-1] + "_s.gif"
        card = PhotoImage(file=cardname)
        cardLabel = Label(frame, image=card, bg="#43ac35")
        cardLabel.image = card
        cardLabel.grid(row=currentplayer.cpu_card_row, column=currentplayer.column_tracker)
    else:
        cardname = "img/" + currentplayer.current_hand_card[-1] + ".gif"
        cardPlayer = PhotoImage(file=cardname)
        cardLabelPlayer = Label(frame, image=cardPlayer, bg="#43ac35")
        cardLabelPlayer.image = cardPlayer
        cardLabelPlayer.grid(row=0, column=currentplayer.column_tracker)
    currentplayer.column_tracker += 1
    #Checks for Aces if player busted
    if sum(currentplayer.current_hand) > 21 and 11 in currentplayer.current_hand:
        currentplayer.current_hand.remove(11)
        currentplayer.current_hand.append(1)


def cpu_beginner(current_player, deck, downcard, playerlist, index_player, frame, upcard):
    #Deal as long as player hand is not 11 or higher
    while sum(current_player.current_hand) < 11:
        playerhit(deck, downcard, playerlist, index_player, current_player, frame, upcard)
        #If player has busted stop dealing
        if sum(current_player.current_hand) > 21:
            return


def cpu_normal(current_player, deck, downcard, playerlist, index_player, frame, upcard):
    #Deal as long as player hand is not 17 or higher
    while sum(current_player.current_hand) <= 17:
        #Hit on a soft 17 but not a hard 17
        if current_player.current_hand == 17:
            if 11 in current_player.current_hand:
                playerhit(deck, downcard, playerlist, index_player, current_player, frame, upcard)
            else:
                return
        else:
            playerhit(deck, downcard, playerlist, index_player, current_player, frame, upcard)
        #If player has busted stop dealing
        if sum(current_player.current_hand) > 21:
            return


def cpu_expert(current_player, deck, downcard, playerlist, index_player, frame, upcard):
    action = chart_strategy_calc(current_player, upcard)
    if action == 'h' or action == 'd':
        playerhit(deck, downcard, playerlist, index_player, current_player, frame, upcard)
    else:
        return


def simulator(round_deck, downcard, playerlist, index_player, upcard, condition, dealer):
    counter = 0
    result_list = []
    loss_count = 0
    win_count = 0
    push_count = 0
    while counter < 100:
        simulator_deck = copy.deepcopy(round_deck)
        simulator_playerlist = copy.deepcopy(playerlist)
        simulator_player_index = index_player
        simulator_dealer = copy.deepcopy(dealer)

        simulator_deck.shuffle()

        if condition == 'h':
            sim_condition = 'h'
            while sim_condition == 'h' or sim_condition == 'd':
                simulator_deck.deal(simulator_playerlist[simulator_player_index])
                sim_condition = chart_strategy_calc(simulator_playerlist[simulator_player_index], upcard)

        inner_counter = simulator_player_index
        while inner_counter < len(simulator_playerlist):
            if simulator_playerlist[inner_counter].status == 'beginner':
                while sum(simulator_playerlist[inner_counter].current_hand) < 11:
                    simulator_deck.deal(simulator_playerlist[inner_counter])
            elif simulator_playerlist[inner_counter].status == 'expert':
                sim_condition_cpu = 'h'
                while sim_condition_cpu == 'h' or sim_condition_cpu == 'd':
                    sim_condition_cpu = chart_strategy_calc(simulator_playerlist[inner_counter], upcard)
                    if sim_condition_cpu == 'h' or sim_condition_cpu == 'd':
                        simulator_deck.deal(simulator_playerlist[inner_counter])
            else:
                while sum(simulator_playerlist[inner_counter].current_hand) < 17:
                    simulator_deck.deal(simulator_playerlist[inner_counter])
            inner_counter += 1

        while sum(simulator_dealer.current_hand) < 17:
            simulator_deck.deal(simulator_dealer)

        player_score = sum(simulator_playerlist[simulator_player_index].current_hand)
        player_length = len(simulator_playerlist[simulator_player_index].current_hand)
        dealer_score = sum(simulator_dealer.current_hand)
        dealer_length = len(simulator_dealer.current_hand)

        if dealer_score == 21 and dealer_score == player_score:
            if dealer_length == 2 and player_length == 2:
                push_count += 1
            elif dealer_length == 2:
                loss_count += 1
            elif player_length == 2:
                win_count += 1
            else:
                push_count += 1
        elif dealer_score == 21 and dealer_length == 2:
            loss_count += 1
        elif player_score == 21 and player_length == 2:
            win_count += 1
        elif dealer_score > 21 and player_score <= 21:
            win_count += 1
        elif player_score > 21:
            loss_count += 1
        elif dealer_score == player_score:
            push_count += 1
        elif player_score > dealer_score:
            win_count += 1
        elif player_score < dealer_score:
            loss_count += 1
        counter += 1
        del simulator_playerlist
        del simulator_deck
        del simulator_dealer
        del simulator_player_index
    return win_count, push_count


def statistic_calc(round_deck, downcard, playerlist, index_player, upcard, dealer, curbet):
    unknown_deck = round_deck.standard_deck
    if downcard != 0:
        unknown_deck.append(downcard)

    #Calculate bust on hit
    bustable_count = 0
    if 11 in playerlist[index_player].current_hand:
        player_score_bust = 31 - sum(playerlist[index_player].current_hand)
    else:
        player_score_bust = 21 - sum(playerlist[index_player].current_hand)
    counter = 0
    while counter < len(unknown_deck):
        if unknown_deck[counter] == 11:
            if player_score_bust < 1:
                bustable_count += 1
        else:
            if player_score_bust < unknown_deck[counter]:
                bustable_count += 1
        counter += 1
    bust_perc = int((bustable_count / len(unknown_deck)) * 100)
    bust_string = "    Bust: " + str(bust_perc) + "%"

    #Find reccomendation
    recom = ""
    re_value = chart_strategy_calc(playerlist[index_player], upcard)
    if re_value == 'h':
        recom = "HIT"
    elif re_value == 's':
        recom == "STAY"
    elif re_value == 'd' or re_value == 'z':
        recom == "DOUBLE"
    elif re_value == 'p':
        recom == "SPLIT"
    else:
        recom == "ERROR"
    recom_out = " Recommend: " + recom

    h_return_perc_w, h_return_perc_d = simulator(round_deck, downcard, playerlist, index_player, upcard, 'h', dealer)
    s_return_perc_w, s_return_perc_d = simulator(round_deck, downcard, playerlist, index_player, upcard, 's', dealer)
    if h_return_perc_w == 100:
        h_return_perc_w = 99
    if h_return_perc_d == 100:
        h_return_perc_d = 99
    if s_return_perc_w == 100:
        s_return_perc_w = 99
    if s_return_perc_d == 100:
        s_return_perc_d = 99
    hit_win = "    Win: " + str(h_return_perc_w) + "%"
    hit_push = "    Push: " + str(h_return_perc_d) + "%"
    stay_win = "    Win: " + str(s_return_perc_w) + "%"
    stay_push = "    Push: " + str(s_return_perc_d) + "%"

    #Display statistics
    statisticFrame = Frame(window, width=375, height= 710, bg="#1b1b1b")
    statisticFrame.place(anchor=SE, relx=1, rely=0.96)
    Label(statisticFrame, text=playerlist[index_player].name, bg="#1b1b1b", fg="white", font="none 23 bold", width=20).grid(row=0)
    Label(statisticFrame, text=curbet, bg="#1b1b1b", fg="white", font="none 23 bold", width=20).grid(row=1)
    Label(statisticFrame, text=" On Hit -", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=2, pady=(100,0))
    Label(statisticFrame, text=hit_win, bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=3)
    Label(statisticFrame, text=hit_push, bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=4)
    Label(statisticFrame, text=bust_string, bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=5)
    Label(statisticFrame, text=" On Stay -", bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=6, pady=(30,0))
    Label(statisticFrame, text=stay_win, bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=7)
    Label(statisticFrame, text=stay_push, bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=8)
    Label(statisticFrame, text=recom_out, bg="#1b1b1b", fg="white", font="none 23 bold", width=20, anchor="w").grid(row=9, pady=(30,100))
    exitButtonsFrame = Frame(statisticFrame, bg="#1b1b1b")
    exitButtonsFrame.grid(row=10, pady=(100,10))
    exitButton = Button(exitButtonsFrame, text="X", font="none 23 bold", command=exitFunc)
    exitButton.grid(row=0, column=2, padx=(10,10))


def busted(user, hitButton, splitButton, doubleButton):
    if sum(user.current_hand) >= 21:
        hitButton.grid_remove()
        splitButton.grid_remove()
        doubleButton.grid_remove()


def doubleDown(round_deck, downcard, playerlist, index_player, current_player, frame, upcard):
    bet = current_player.current_bet
    money = current_player.money
    if money >= bet:
        current_player.money -= bet
        current_player.current_bet = 2 * bet
        playerhit(round_deck, downcard, playerlist, index_player, current_player, frame, upcard)
##############################################################################################################################################

# BLACKJACK ROUND MANAGER ####################################################################################################################
#Begins and manages the rounds of blackjack, makes calls to the game logic
def blackjack_round(playerlist):
    round_deck = Deck()
    round_deck.shuffle()

    #Burn card per Blackjack rules
    del round_deck.standard_deck[0]

    #Recieve Bets
    for i in playerlist:
        if i.status != 'user':
            if i.money >= 50:
                i.current_bet = 50
                i.money -= 50
        #Ask user for bet
        else:
            #Create background
            background = PhotoImage(file="img/background.gif")
            Label(window, image=background, bg="#43ac35").place(x=0, y=0, relwidth=1, relheight=1)
            #Create bet slider
            cur_money = i.money
            int_money = int(cur_money / 10)
            Label(window, text="Enter Bet:", bg="#43ac35", fg="white", font="none 25 bold").grid(row=0, column=0, padx=(200,20), pady=(150,0))
            bet = Scale(window, from_=10, to=cur_money, orient="horizontal", bg="#43ac35", fg="white", font="none 17 bold", tickinterval=int_money, length=1000)
            bet.set(int_money)
            bet.grid(row=0, column=1, pady=(150,0))
            wait_bet = IntVar()
            bet_button = Button(window, text="Place Bet", font="none 17 bold", command=lambda: wait_bet.set(1))
            bet_button.grid(row=0, column=2, pady=(150,0), padx=(20,0))
            bet_button.wait_variable(wait_bet)

            i.current_bet = bet.get()
            curbet = "Bet - $" + str(bet.get())
            i.money -= bet.get()

    #Initialize Dealer
    dealer = Player('dealer', 1000000, 'normal')
    downcard = 0
    upcard = 0

    #Find index of User in playerlist
    index_player = 0
    new_counter = 0
    for i in playerlist:
        if i.status == 'user':
            index_player = new_counter
        new_counter += 1

    #Deal
    for i in playerlist:
        round_deck.deal(i)
    #Give dealer his down-card
    round_deck.deal(dealer)
    downcard = dealer.current_hand[0]
    downcard_suit = dealer.current_hand_card[0]
    for i in playerlist:
        round_deck.deal(i)
    #Give dealer his up-card
    round_deck.deal(dealer)
    upcard = dealer.current_hand[1]

    #Create main round screen
    #Create background
    background = PhotoImage(file="img/background.gif")
    backing = Label(window, image=background, bg="#43ac35")
    backing.image = background
    backing.place(x=0, y=0, relwidth=1, relheight=1)

    #CPU name and hand show
    cpuplayers = Frame(window, bg="#43ac35")
    cpuplayers.place(anchor=W, relx=0.02, y=410)
    cpu_count = 0
    for i in playerlist:
        if i.status != 'user':
            cpuLab = str(i.name) + " - $" + str(int(i.money))
            Label(cpuplayers, text=cpuLab, bg="#43ac35", fg="white", font="none 20 bold").grid(row=cpu_count, column=0, columnspan=4)
            counter = 0
            while counter < len(i.current_hand_card):
                cardname = "img/" + i.current_hand_card[counter] + "_s.gif"
                card = PhotoImage(file=cardname)
                cardLabel = Label(cpuplayers, image=card, bg="#43ac35")
                cardLabel.image = card
                cardLabel.grid(row=(cpu_count+1), column=counter)
                counter += 1
                i.column_tracker = counter
                i.cpu_card_row = cpu_count + 1
            cpu_count += 2

    #Display Dealer's hand
    dealercards = Frame(window, bg="#43ac35")
    dealercards.place(relx=0.12, rely=0)
    #Display first Dealer's card facedown
    cardDealerDown = PhotoImage(file="img/back.gif")
    cardLabelDealerDown = Label(dealercards, image=cardDealerDown, bg="#43ac35")
    cardLabelDealerDown.image = cardDealerDown
    cardLabelDealerDown.grid(row=0, column=0)
    counter = 1
    while counter < len(dealer.current_hand_card):
        cardname = "img/" + dealer.current_hand_card[counter] + ".gif"
        cardDealer = PhotoImage(file=cardname)
        cardLabelDealer = Label(dealercards, image=cardDealer, bg="#43ac35")
        cardLabelDealer.image = cardDealer
        cardLabelDealer.grid(row=0, column=counter)
        counter += 1
        dealer.column_tracker = counter

    #Display Player's hand
    for i in playerlist:
        if i.status == 'user':
            playercards = Frame(window, bg="#43ac35")
            playercards.place(anchor=SW, relx=0.14, rely=0.95)
            counter = 0
            while counter < len(i.current_hand_card):
                cardname = "img/" + i.current_hand_card[counter] + ".gif"
                cardPlayer = PhotoImage(file=cardname)
                cardLabelPlayer = Label(playercards, image=cardPlayer, bg="#43ac35")
                cardLabelPlayer.image = cardPlayer
                cardLabelPlayer.grid(row=0, column=counter)
                counter += 1
                i.column_tracker = counter

    #Display current money of Player
    moneyFrame = Frame(window)
    moneyFrame.place(anchor=NE, relx=0.99, rely=0)
    curmoney = "$" + str(playerlist[index_player].money)
    Label(moneyFrame, text=curmoney, bg="#43ac35", fg="white", font="none 23 bold").grid(row=0)

    #Check dealer Blackjack
    if sum(dealer.current_hand) == 21:
        end_condition, player_money, temp_playerlist = end_round(dealer, playerlist, round_deck)

    #Begin players turns
    player_count = 0
    while player_count < index_player:
        if playerlist[player_count].status == 'beginner':
            cpu_beginner(playerlist[player_count], round_deck, downcard, playerlist, index_player, cpuplayers, upcard)
        elif playerlist[player_count].status == 'expert':
            cpu_expert(playerlist[player_count], round_deck, downcard, playerlist, index_player, cpuplayers, upcard)
        else:
            cpu_normal(playerlist[player_count], round_deck, downcard, playerlist, index_player, cpuplayers, upcard)
        player_count += 1

    #Players turn
    statistic_calc(round_deck, downcard, playerlist, index_player, upcard, dealer, curbet)
    #Player action button
    actionFrame = Frame(window, width=230, height=215, bg="#43ac35")
    actionFrame.place(anchor=SW, relx=0.01, rely=0.95)
    hitButton = Button(actionFrame, text="HIT", bg='green', fg='white', font="none 20 bold", width=13, command=lambda: [playerhit(round_deck, downcard, playerlist, index_player, playerlist[index_player], playercards, upcard), busted(playerlist[index_player], hitButton, splitButton, doubleButton), statistic_calc(round_deck, downcard, playerlist, index_player, upcard, dealer, curbet)])
    hitButton.grid(row=0)
    wait_stay = IntVar()
    stayButton = Button(actionFrame, text="STAY", bg='red', fg='white', font="none 20 bold", width=13, command=lambda: [wait_stay.set(1), hitButton.grid_remove(), stayButton.grid_remove(), doubleButton.grid_remove(), splitButton.grid_remove()])
    stayButton.grid(row=1)
    doubleButton = Button(actionFrame, text="DOUBLE", bg='blue', fg='white', font="none 20 bold", width=13, command=lambda: [doubleDown(round_deck, downcard, playerlist, index_player, playerlist[index_player], playercards, upcard), wait_stay.set(1), hitButton.grid_remove(), stayButton.grid_remove(), doubleButton.grid_remove(), splitButton.grid_remove()])
    if playerlist[index_player].money >= playerlist[index_player].current_bet:
        doubleButton.grid(row=2)
    #splitButton = Button(actionFrame, text="SPLIT", bg='purple', fg='white', font="none 20 bold", width=13, command=lambda: [wait_stay.set(1), hitButton.grid_remove(), stayButton.grid_remove(), doubleButton.grid_remove(), splitButton.grid_remove()])
    #if playerlist[index_player].current_hand[0] == playerlist[index_player].current_hand[1]:
        #splitButton.grid(row=3)
    stayButton.wait_variable(wait_stay)

    #Finish players turns
    player_count += 1
    while player_count < len(playerlist):
        if playerlist[player_count].status == 'beginner':
            cpu_beginner(playerlist[player_count], round_deck, downcard, playerlist, index_player, cpuplayers, upcard)
        elif playerlist[player_count].status == 'expert':
            cpu_expert(playerlist[player_count], round_deck, downcard, playerlist, index_player, cpuplayers, upcard)
        else:
            cpu_normal(playerlist[player_count], round_deck, downcard, playerlist, index_player, cpuplayers, upcard)
        player_count += 1

    #Dealers turn
    cpu_normal(dealer, round_deck, downcard, playerlist, index_player, dealercards, upcard)

    #Flip the dealers downcard
    downcard_file = "img/" + downcard_suit + ".gif"
    cardDealerDown = PhotoImage(file=downcard_file)
    cardLabelDealerDown = Label(dealercards, image=cardDealerDown, bg="#43ac35")
    cardLabelDealerDown.image = cardDealerDown
    cardLabelDealerDown.grid(row=0, column=0)

    end_condition, player_money, temp_playerlist = end_round(dealer, playerlist, round_deck)

    endGameFrame = Frame(window, bg="#1b1b1b")
    endGameFrame.place(relx="0.4", rely="0.45")
    Label(endGameFrame, text=end_condition, bg="#1b1b1b", fg="white", font="none 30 bold", width="20").grid()
    endRound_wait = IntVar()
    NextRoundButton = Button(endGameFrame, text="NEXT ROUND", font="none 20 bold", command=lambda: endRound_wait.set(1))
    NextRoundButton.grid()
    NextRoundButton.wait_variable(endRound_wait)

    return player_money, temp_playerlist
##############################################################################################################################################

# GAME MANAGEMENT & DISPLAY FUNCTIONS ########################################################################################################
#The main game function, controls the flow of the game
def game_manager(playerlist, playerMoneyTracker):
    #Allows the player to continue playing rounds of blackjack until player is out of money
    while playerMoneyTracker > 0:
        playerMoneyTracker, temp_playerlist = blackjack_round(playerlist)
        playerlist = copy.deepcopy(temp_playerlist)

    #After the game is over display game over
    #Create background
    background = PhotoImage(file="img/background.gif")
    backing = Label(window, image=background, bg="#43ac35")
    backing.image = background
    backing.place(x=0, y=0, relwidth=1, relheight=1)
    endGameFrame = Frame(window, bg="#1b1b1b")
    endGameFrame.place(relx="0.4", rely="0.7")
    Label(endGameFrame, text="GAME OVER", bg="#1b1b1b", fg="white", font="none 30 bold", width="20").grid()
    endRound_wait = IntVar()
    NextRoundButton = Button(endGameFrame, text="EXIT", font="none 20 bold", command=lambda: endRound_wait.set(1))
    NextRoundButton.grid()
    NextRoundButton.wait_variable(endRound_wait)

    sys.exit()


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
window.title("Blackjack Casino (V 2.2.0)")
window.configure(background="black")
window.geometry('1920x1080')

#Create background
background = PhotoImage(file="img/background.gif")
Label(window, image=background, bg="#43ac35").place(x=0, y=0, relwidth=1, relheight=1)

#Call Splash Screen start
splash_screen()

#run main loop
window.mainloop()
##############################################################################################################################################
