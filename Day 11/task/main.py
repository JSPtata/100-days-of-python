import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    if sum(hand)==21 and len(hand)==2:
        return 0
    if 11 in hand and sum(hand)>21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "Both went over.You lose!"
    elif user_score==computer_score:
        return "It's a draw."
    elif user_score==0:
        return"You win with a blackjack!"
    elif computer_score==0:
        return "You lose! Opponent has a blackjack."
    elif user_score>21:
        return "You went over.You lose."
    elif computer_score>21:
        return "Computer went over.You win!"
    elif user_score>computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_cards=[]
    computer_cards=[]
    is_game_over=False

    print(art.logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"Your cards: [{user_cards}],current_score: {user_score}")
        print(f"Computer's first card: [{computer_cards[0]}]")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            another_choice=input(" Type 'y' to get another card, type 'n' to pass: ")
            if another_choice=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while calculate_score(computer_cards)<17:
        computer_cards.append(deal_card())

    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    print(f"\nYour final hand: [{user_cards}],final score: {user_score}")
    print(f"Computer final hand: [{computer_cards}],final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("\nDo you want to play a game of blackjack? Type 'y' or 'n': ")=='y':
        print("\n"*50)
        play_game()






