# Blackjack Betting Strategy Simulator

## Project Overview

This project implements a simulation of a blackjack game using multiple decks of cards, card counting, and a customizable betting strategy based on a player's blackjack hand and the dealer's face-up card. The goal is to allow users to simulate various strategies, run multiple iterations of the game, and optimize betting strategies based on outcomes.

The main components of this project include:
- Simulating a blackjack game with basic rules.
- Implementing a strategy for when to hit or stay based on a defined blackjack strategy.
- Simulating card counting with multiple decks of cards.
- Implementing and optimizing a betting strategy based on card counting.

## Key Features

- **Card Counting:** The game supports basic card counting, which adjusts the player's betting strategy based on the count of high or low cards remaining in the deck.
- **Betting Strategy:** The betting strategy is defined by a dictionary that maps the card count to the amount of money to bet. You can customize this strategy as needed.
- **Blackjack Strategy:** A predefined blackjack strategy is provided that dictates whether the player should hit or stand based on their hand and the dealer's visible card.
- **Optimization:** The project includes an optimization function that attempts to improve the betting strategy by adjusting the bet amounts to maximize profits over many iterations.

## Project Structure

1. **`main.py`**  
   The entry point of the program, where the game is initialized and run.
   
   - It uses the `Game` class to simulate a full day of blackjack with a predefined number of iterations.
   - It allows the user to set the number of decks, whether to use card counting, and the number of iterations for the simulation.
   - The game runs, and the player's betting strategy is adjusted based on the card count.

2. **`game.py`**  
   Contains the `Game` class which simulates the game logic.

   - **`n_decks`**: Represents multiple decks of cards and manages the card count.
   - **`Game`**: The core class that manages the betting strategy, runs the blackjack game, and tracks the results over multiple hands.
   - **`run_day`**: Simulates a full day of blackjack by iterating through hands and adjusting the player's portfolio based on the game results and betting strategy.
   - **`optimize_betting_strategy`**: A method that optimizes the betting strategy using a basic iterative approach to maximize the portfolio outcome.

3. **`utils.py`**  
   Contains utility functions for blackjack strategy and hand management.

   - **`first_hand`**: Determines the initial decision for the player based on the strategy dictionary.
   - **`next_hands`**: Determines if the player should hit or stay after the first move.
   - **`sum_hand`**: Calculates the possible values of the player's hand, accounting for aces that can be 1 or 11.
   - **`blackjack_strategy`**: A dictionary that defines the basic blackjack strategy based on player hands and dealer’s visible cards.

#  Blackjack Simulation Project

## Overview

This project simulates a game of Blackjack with an emphasis on betting strategies and card counting. The simulation involves multiple rounds of Blackjack, and the betting amount is adjusted based on a simple card-counting strategy and predefined betting rules. The simulation also includes an optimization feature to adjust the betting strategy for improved results.

## Key Components

	1.	main.py: This is the entry point for running the simulation. It sets up the game with a specific betting strategy, Blackjack strategy, and game parameters. You can configure the number of decks, when to reset the deck, and how many iterations the simulation should run.
	2.	game.py: Contains the core logic of the Blackjack game and deck management. The game class simulates a Blackjack game with card counting and runs multiple iterations (games). The n_decks class manages the deck of cards, including drawing cards and counting them for card counting.
	3.	utils.py: Includes helper functions and the Blackjack strategy dictionary, which outlines the recommended actions based on the player’s hand and the dealer’s visible card. This file contains functions for determining the next move (first_hand and next_hands) and calculating the sum of a hand (sum_hand).

## How to Use



###	Set Up Betting Strategy:
In the main.py file, define your betting strategy using a dictionary where the key represents the card count and the value represents the amount to bet:
```python
win_betting_strategy = {0: 0, 1: 1, 2: 2, 3: 4, 4: 4, 5: 12}
```

###	Configure the Game:
You can configure the game parameters when creating a new game object in main.py. The available options include:
	•	number_decks: The number of decks used in the game (default is 6).
	•	reset_deck: The number of decks left before resetting the shoe (default is 2).
	•	nb_iter: The number of game iterations (default is 10000).
	•	counting_cards: Whether to enable card counting (default is True).
Example:

mygame = game(win_betting_strategy, blackjack_strategy, number_decks=6, reset_deck=2, nb_iter=10000, counting_cards=True)


###	Run the Simulation:
To run a single day of games (e.g., 10,000 iterations):
```python
mygame.run_day(iters=10000)
```
This will print the ratio of successful games when the card count is positive vs. negative, and also the overall portfolio outcome.

### Optimize Betting Strategy (Optional):
You can try optimizing the betting strategy by adjusting the bet amounts using gradient-based optimization:
```python
mygame.optimize_betting_strategy(learning_rate=0.1, iterations=100)
```
This will adjust the betting amounts to maximize the portfolio value over several iterations.

## Files Breakdown

 1. main.py

This file is the entry point to the program. It allows you to:

	•	Define the betting strategy.
	•	Configure the game with the number of decks, reset threshold, and iterations.
	•	Run the game and print results.

2. game.py

	•	n_decks Class: Manages the deck of cards. It keeps track of the number of cards left, deals cards, and implements basic card-counting functionality.
	•	game Class: The core class that simulates Blackjack rounds, including player and dealer hands, determining the winner, and updating the betting portfolio based on the result.

3. utils.py

Contains:

	•	blackjack_strategy: A dictionary with predefined rules for actions (hit/stand) based on the player’s hand and the dealer’s face-up card.
	•	first_hand: Determines the first move for the player’s hand.
	•	next_hands: Determines the next move as more cards are drawn.
	•	sum_hand: Calculates the total value of a player’s hand.

## Example Usage

Here is a quick example of how to use the project:
```python
from Game import game
from utils import blackjack_strategy

win_betting_strategy = {0: 0, 1: 1, 2: 2, 3: 4, 4:4, 5: 12}

mygame = game(win_betting_strategy, blackjack_strategy, number_decks=6, reset_deck=2, nb_iter=10000, counting_cards=True)
mygame.run_day(iters=10000)
```

This example sets up a Blackjack game with 6 decks, resets the deck when only 2 decks are left, and runs 10,000 iterations of the game using card counting. The betting strategy is defined in the win_betting_strategy dictionary.