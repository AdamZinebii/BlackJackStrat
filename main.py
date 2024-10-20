from Game import game
from utils import blackjack_strategy

win_betting_strategy = {0: 0, 1: 1, 2: 2, 3: 4, 4:4, 5: 12}

mygame = game(win_betting_strategy, blackjack_strategy, number_decks=6, reset_deck=2, nb_iter=10000, counting_cards=True)
mygame.run_day(iters=10000)
