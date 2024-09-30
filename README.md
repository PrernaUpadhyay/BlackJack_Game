

# Blackjack Game

Welcome to the Blackjack Game! This is a simple command-line implementation of the classic card game Blackjack, where players try to get a hand value as close to 21 as possible without exceeding it.



## Features

- Play against a dealer in a simple command-line interface.
- Supports the basic rules of Blackjack, including hitting, standing, and busting.
- Automatically handles Ace cards as either 1 or 11 based on the hand's total value.
- Displays ASCII art for cards and the game logo.

## Installation

To run the Blackjack game, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).



## How to Play

1. When prompted, choose to play the game by typing 'y' for yes or 'n' for no.
2. You will be dealt two cards, and the dealer will also receive two cards (one card is hidden).
3. Your goal is to get as close to 21 as possible without going over.
4. You can choose to "hit" (take another card) or "stand" (keep your current hand).
5. The dealer will then play according to the rules (hitting until reaching at least 17).
6. The winner is determined based on who is closer to 21 without exceeding it.

## Gameplay

- **Hit**: Draw another card to increase your hand value.
- **Stand**: End your turn and let the dealer play.
- **Bust**: If your hand value exceeds 21, you lose.
- **Blackjack**: A hand value of 21 with the initial two cards is a winning condition.

### Example Gameplay

```
Do you want to play a game of Blackjack? Type 'y' or 'n': y

Welcome to Blackjack! 🃏
Your hand:
┌─────────┐ ┌─────────┐
│A        │ │K        │
│         │ │         │
│    11   │ │    10   │
│         │ │         │
│        A│ │        K│
└─────────┘ └─────────┘
Your current score: 21 🎯

Dealer's hand:
┌─────────┐ ┌─────────┐
│?        │ │8        │
│         │ │         │
│    ?    │ │    8    │
│         │ │         │
│        ?│ │        8│
└─────────┘ └─────────┘
```


