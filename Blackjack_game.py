import random

# Card values: Dictionary mapping card faces to their numerical values
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# ASCII art for the game logo (using a raw string to avoid escape sequence warnings)
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    """Randomly select and return a card from the deck."""
    return random.choice(list(cards.keys()))


def calculate_score(hand):
    """
    Calculate the score of a hand.
    Special rule: If an Ace is present and the score is over 21,
    count the Ace as 1 instead of 11.
    """
    score = sum(cards[card] for card in hand)
    if 'A' in hand and score > 21:
        score -= 10  # Count Ace as 1 instead of 11
    return score


def display_cards(hand, hide_first=False):
    """
    Generate ASCII art representation of cards in a hand.
    If hide_first is True, the first card will be hidden (for dealer's initial hand).
    """
    card_art = [
        "┌─────────┐",
        "│{}        │",
        "│         │",
        "│    {}    │",
        "│         │",
        "│        {}│",
        "└─────────┘"
    ]

    lines = [[] for _ in range(7)]
    for i, card in enumerate(hand):
        if i == 0 and hide_first:
            card = "?"
        card_lines = [line.format(card.ljust(2), card.center(2), card.rjust(2)) for line in card_art]
        for j, line in enumerate(card_lines):
            lines[j].append(line)

    return "\n".join(" ".join(line) for line in lines)


def play_game():
    """Main game logic for a single round of Blackjack."""
    print(logo)  # Display the game logo
    print("Welcome to Blackjack! 🃏")
    player_hand = []
    dealer_hand = []

    # Initial deal: 2 cards each for player and dealer
    player_hand.extend([deal_card(), deal_card()])
    dealer_hand.extend([deal_card(), deal_card()])

    # Calculate initial scores
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    # Display initial hands
    print("\nDealer's hand:")
    print(display_cards(dealer_hand, hide_first=True))
    print("\nYour hand:")
    print(display_cards(player_hand))
    print(f"Your current score: {player_score} 🎯")

    # Check for Blackjack (21 with initial two cards)
    if player_score == 21 or dealer_score == 21:
        print("\nFinal hands:")
        print("Dealer's hand:")
        print(display_cards(dealer_hand))
        print(f"Dealer's score: {dealer_score}")
        print("\nYour hand:")
        print(display_cards(player_hand))
        print(f"Your score: {player_score}")

        if player_score == 21 and dealer_score == 21:
            print("Both have Blackjack! It's a tie! 🎭")
        elif player_score == 21:
            print("Blackjack! You win! 🎉🏆")
        else:
            print("Dealer has Blackjack! You lose. 😢")
        return

    # Player's turn
    while True:
        # Check for player bust
        if player_score > 21:
            print("Bust! You lose. 💥😢")
            return

        # Player decides to hit or stand
        action = input("Do you want to hit 🃏 or stand 🛑? ").lower()
        if action == 'hit':
            player_hand.append(deal_card())
            player_score = calculate_score(player_hand)
            print("\nYour hand:")
            print(display_cards(player_hand))
            print(f"Your current score: {player_score} 🎯")
        elif action == 'stand':
            break

    # Dealer's turn: hit until score is at least 17
    print("\nDealer's turn... 🤖")
    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    # Show final hands
    print("\nDealer's final hand:")
    print(display_cards(dealer_hand))
    print(f"Dealer's final score: {dealer_score} 🎯")

    print("\nYour final hand:")
    print(display_cards(player_hand))
    print(f"Your final score: {player_score} 🎯")

    # Determine winner
    if dealer_score > 21:
        print("Dealer busts! You win! 🎉🏆")
    elif player_score > dealer_score:
        print("You win! 🎉🏆")
    elif player_score < dealer_score:
        print("Dealer wins! 😢")
    else:
        print("It's a tie! 🎭")


# Game loop: keep playing new games until the player decides to stop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" *20)
    play_game()

print("Thanks for playing! 👋")