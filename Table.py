from Shoe import *
from Hand import Hand

import time

print("Welcome to blackjack!")
print("Let's play!")
balance = 100
print("Your balance is 100")
shoe = Shoe()

def play_hand(dealer: bool, hand:Hand):

    if dealer:
        print
        while(hand.total < 17):
            hand.add_card(shoe.draw_card())
        for i in range(1,len(hand.cards)):
            print("Dealer has: ",hand.show_cards()[:i])
            time.sleep(2)
        print("Dealer has: ", hand.show_cards(), " : ", hand.total)
        return
    if hand.total > 21:
        print("Player BUST: ", hand.show_cards(), " : ", hand.total)
        return

    print("Player : ", hand.show_cards(), " : ", hand.total)
    options = ["Hit(h)", "Stand(s)"]
    accept = ["h", "s", "d"]
    if len(hand.cards) == 2:
        options.append("Double(d)")
        accept.append("d")
        if hand.cards[0]['rank'] == hand.cards[1]['rank']:
            options.append("Split(sp)")
            accept.append("sp")
    move = ""
    while(True):
        move = str(input("What's your move: "))
        if move not in accept:
            print("Not a valid move")
        else:
            break

    if move == "s":
        return
    if move == "d":
        hand.stake *= 2
        hand.add_card(shoe.draw_card())
        print("Player : ", hand.show_cards(), " : ", hand.total)
        return
    if move == "h":
        hand.add_card(shoe.draw_card())
        play_hand(dealer, hand)
    if move == "sp":
        print("not fuckin done yet")



while(not shoe.dead):
    while True:
        try:
            bet = int(input(f"Enter your bet: between 0 and {balance}: "))
            if 0 <= bet <= balance:
                break
            else:
                print("Error: Input must be within the specified range.")
        except ValueError:
            print("Error: Input must be a valid integer.")

    player_hand = Hand(bet)
    dealer_hand = Hand(0)
    player_hand.add_card(shoe.draw_card())
    dealer_hand.add_card(shoe.draw_card())
    player_hand.add_card(shoe.draw_card())
    dealer_hand.add_card(shoe.draw_card())
    print("Dealer has: ", dealer_hand.cards[0]['rank'])
    print("Player has: ", player_hand.show_cards())
    
    if player_hand.total == 21:
        print("Blackjack! Now let's see what the dealer has")
        if dealer_hand.total == 21:
            print("You got Greg'd, dealer has 21!")
            continue
        else:
            print("Well done!")
            balance += 1.5*player_hand.stake
            continue
    play_hand(False, player_hand)
    if player_hand.bust:
        print("Dealer had: ", dealer_hand.show_cards())
        balance -= player_hand.stake
    else:
        play_hand(True, dealer_hand)
        if dealer_hand.bust:
            print("Dealer busts!")
            balance += player_hand.stake
        elif player_hand.total == dealer_hand.total:
            print("Push")
        elif player_hand.total > dealer_hand.total:
            print("You win!")
            balance += player_hand.stake
        else:
            print("Dealer wins!")
            balance -= player_hand.stake
