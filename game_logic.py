import random


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




#Helper Functions
def cpu_play(current_player, deck, dealer_upcard = 0): #CPU logic that controls CPU Players
    if current_player.status == "beginner":
        #Deal as long as player hand is not 11 or higher
        while sum(current_player.current_hand) < 11:
            deck.deal(current_player)
            #Checks for Aces if player busted
            if sum(current_player.current_hand) > 21 and 11 in current_player.current_hand:
                current_player.current_hand.remove(11)
                current_player.current_hand.append(1)
            #If player has busted stop dealing
            if sum(current_player.current_hand) > 21:
                return
    elif current_player.status == "normal":
        #Deal as long as player hand is not 17 or higher
        while sum(current_player.current_hand) <= 17:
            #Hit on a soft 17 but not a hard 17
            if current_player.current_hand == 17:
                if 11 in current_player.current_hand:
                    deck.deal(current_player)
                else:
                    return
            else:
                deck.deal(current_player)
            #Checks for Aces if player busted
            if sum(current_player.current_hand) > 21 and 11 in current_player.current_hand:
                current_player.current_hand.remove(11)
                current_player.current_hand.append(1)
            #If player has busted stop dealing
            if sum(current_player.current_hand) > 21:
                return
    else:
        return_value = True
        while return_value:
            #Checks if the player has a soft total
            if 11 in current_player.current_hand:
                #If the dealer is showing 9 or higher
                if dealer_upcard >= 9:
                    #If the player's hand is less then or equal to 18, hit
                    if sum(current_player.current_hand) <= 18:
                        deck.deal(current_player)
                    #If player has over 18, stay
                    else:
                        return_value = False
                        return
                #If the dealer is showing a 7 or 8
                elif dealer_upcard in range(7,9):
                    #If the player's hand is less then or equal to 17, hit
                    if sum(current_player.current_hand) <= 17:
                        deck.deal(current_player)
                    #If player has over 17, stay
                    else:
                        return_value = False
                        return
                #If the dealer is showing a 6
                elif dealer_upcard == 6:
                    #If the player has a 20 or higher, stay
                    if sum(current_player.current_hand) >= 20:
                        return_value = False
                        return
                    #If the player has less then 20 double
                    else:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If the player doesnt have money to double but has under or equal to 17, hit
                        elif sum(current_player.current_hand) <= 17:
                            deck.deal(current_player)
                        #If the player doesnt have money to double but has over 17, stay
                        else:
                            return_value = False
                            return
                #If the dealer is showing a 5
                elif dealer_upcard == 5:
                    #If the player has a 19 or higher, stay
                    if sum(current_player.current_hand) >= 19:
                        return_value = False
                        return
                    #If the player has less then 19 double
                    else:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If the player doesnt have money to double but has under or equal to 17, hit
                        elif sum(current_player.current_hand) <= 17:
                            deck.deal(current_player)
                        #If the player doesnt have money to double but has over 17, stay
                        else:
                            return_value = False
                            return
                elif dealer_upcard == 4:
                    #If the player has a 19 or higher, stay
                    if sum(current_player.current_hand) >= 19:
                        return_value = False
                        return
                    #If the player has a 14 or less, hit
                    elif sum(current_player.current_hand) <= 14:
                        deck.deal(current_player)
                    else:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player cant double and has a 18, stay
                        elif sum(current_player.current_hand) == 18:
                            return_value = False
                            return
                        #If a player cant double but doesnt have 18, hit
                        else:
                            deck.deal(current_player)
                elif dealer_upcard == 3:
                    #If the player has a 19 or higher, stay
                    if sum(current_player.current_hand) >= 19:
                        return_value = False
                        return
                    #If the player has a 16 or less, hit
                    elif sum(current_player.current_hand) <= 16:
                        deck.deal(current_player)
                    else:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player cant double and has a 18, stay
                        elif sum(current_player.current_hand) == 18:
                            return_value = False
                            return
                        #If a player cant double but doesnt have 18, hit
                        else:
                            deck.deal(current_player)
                else:
                    #If the player has a 19 or higher, stay
                    if sum(current_player.current_hand) >= 19:
                        return_value = False
                        return
                    #If the player has a 17 or less, hit
                    elif sum(current_player.current_hand) <= 17:
                        deck.deal(current_player)
                    else:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player cant double and has a 18, stay
                        else:
                            return_value = False
                            return
            #If the player has a hard total
            else:
                #If the dealer is showing 10 or higher
                if dealer_upcard >= 10:
                    #If the player has 17 or more then stay
                    if sum(current_player.current_hand) <= 17:
                        return_value = False
                        return
                    #If the player has 11 try to double down
                    elif sum(current_player.current_hand) == 11:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player can't double down, hit
                        else:
                            deck.deal(current_player)
                    #If the plaer doesnt have over 17 or an 11, hit
                    else:
                        deck.deal(current_player)
                #If the dealer is showing 7 to 9
                elif dealer_upcard in range(7, 10):
                    #If the player has 17 or more then stay
                    if sum(current_player.current_hand) <= 17:
                        return_value = False
                        return
                    #If player has 10 or 11 try to double
                    elif sum(current_player.current_hand) == 10  or sum(current_player.current_hand) == 11:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player can't double down, hit
                        else:
                            deck.deal(current_player)
                    #If the player doesnt have over 17 or an 10 or 11, hit
                    else:
                        deck.deal(current_player)


                #If the dealer is showing 4 to 6
                elif dealer_upcard in range(4, 7):
                    #If the player has 12 or more then stay
                    if sum(current_player.current_hand) <= 12:
                        return_value = False
                        return
                    #If player has 9 to 11 try to double
                    elif sum(current_player.current_hand) in range(9, 12):
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player can't double down, hit
                        else:
                            deck.deal(current_player)
                    #If the player has 8 or less, hit
                    else:
                        deck.deal(current_player)
                #If the dealer is showing a 4
                elif dealer_upcard == 4:
                    #If the player has 13 or more then stay
                    if sum(current_player.current_hand) <= 13:
                        return_value = False
                        return
                    #If player has 9 to 11 try to double
                    elif sum(current_player.current_hand) in range(9, 12):
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player can't double down, hit
                        else:
                            deck.deal(current_player)
                    #If the player has 8 or less or 12, hit
                    else:
                        deck.deal(current_player)
                #If the dealer is showing a 3
                elif dealer_upcard == 3:
                    #If the player has 13 or more then stay
                    if sum(current_player.current_hand) <= 13:
                        return_value = False
                        return
                    #If player has 10 or 11 try to double
                    elif sum(current_player.current_hand) == 10  or sum(current_player.current_hand) == 11:
                        #If player has money to double do so
                        if current_player.money >= current_player.current_bet:
                            current_player.current_bet = 2 * current_player.current_bet
                            current_player.money -= urrent_player.current_bet
                            deck.deal(current_player)
                            return_value = False
                            return
                        #If player can't double down, hit
                        else:
                            deck.deal(current_player)
                    #If the player has 9 or less or 12, hit
                    else:
                        deck.deal(current_player)
            #Check for bust
            if sum(current_player.current_hand) >= 21:
                #Check if Ace is in hand
                if 11 in current_player.current_hand:
                    current_player.current_hand.remove(11)
                    current_player.current_hand.append(1)
                    #After shifting with soft total, recheck bust
                    if sum(current_player.current_hand) >= 21:
                        return_value = False
                        return
                #If busted end turn
                else:
                    return_value = False
                    return



def round_end(): #Finilization and Cleanup at the round end
    for i in playerlist:
        i.current_hand.clear()
        i.current_bet = 0







def temp_out(dealer, playerlist):
    print("------------------------------------------------------------------------------------")
    print("Dealers: ", dealer.current_hand, " - score: ", sum(dealer.current_hand))
    for i in playerlist:
        print(i.name,": ", i.current_hand, " - score: ", sum(i.current_hand), " - Total Money: ", i.money)
    print("------------------------------------------------------------------------------------")




def round(playerlist):
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
        else:
            #Ask user for bet
            ########################################################################################################
            i.currentbet = input("Place your bet: ")
            i.money -= 100

    #Initialize Dealer
    dealer = Player('dealer', 1000000, 'normal')

    #Deal
    for i in playerlist:
        round_deck.deal(i)
    #Give dealer his down-card
    round_deck.deal(dealer)
    for i in playerlist:
        round_deck.deal(i)
    #Give dealer his up-card
    round_deck.deal(dealer)

    #Dealer Blackjack check off draw
    if sum(dealer.current_hand) == 21:
        for i in playerlist:
            #If player also has blackjack, push
            if sum(i.current_hand) == 21:
                i.money += i.current_bet
            #If player doesn't have blackjack, loss
            else:
                i.money -= i.current_bet
        round_end()

    #Begin playing round
    for i in playerlist:
        if i.status != 'user':
            cpu_play(i, round_deck, dealer.current_hand[1])
        else:
            #Let user play
            ########################################################################################################
            temp_input = 'a'
            while temp_input != 's':
                print("Dealer Card: ", dealer.current_hand[1])
                print("Current Hand: ", i.current_hand)
                temp_input = input("Hit or Stay: ('h' or 's') ")
                if temp_input == 'h':
                    round_deck.deal(i)


    #Complete Dealers turn
    cpu_play(dealer, round_deck)

    #Check for winners
    #Checks if dealer busts
    if sum(dealer.current_hand) > 21:
        for i in playerlist:
            #if dealer busts and player doesnt pay out
            if sum(i.current_hand) < 21:
                i.money += (2 * i.current_bet)
            elif sum(i.current_hand) == 21:
                #If player gets blackjack pay out 3 to 2
                if len(i.current_hand) == 2:
                    i.money += (i.current_bet + (1.5 * i.current_bet))
                else:
                    i.money += (2 * i.current_bet)
    #If dealer didn't bust check totals
    else:
        for i in playerlist:
            if sum(i.current_hand) > sum(dealer.current_hand):
                #If player gets blackjack pay out 3 to 2
                if sum(i.current_hand) == 21 and len(i.current_hand) == 2:
                    i.money += (i.current_bet + (1.5 * i.current_bet))
                elif sum(i.current_hand) <= 21:
                    i.money += (2 * i.current_bet)
            #If player and dealer push return bet
            elif sum(i.current_hand) == sum(dealer.current_hand):
                i.money += i.current_bet

    #Call round end
    temp_out(dealer, playerlist)##############################################################
    round_end()



###########################################################################################
###################################################################################################
user = Player('user', 1000, 'user')
cpu1 = Player('CPU1', 1000, 'beginner')
cpu2 = Player('CPU2', 1000, 'normal')
cpu3 = Player('CPU3', 1000, 'expert')
playerlist = [user, cpu1, cpu2, cpu3]
round(playerlist)
