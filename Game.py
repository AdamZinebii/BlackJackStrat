from utils import first_hand, sum_hand, next_hands
import random


class n_decks:
    def __init__(self, n):
        self.n = n
        self.card_contents = {'A': n * 4, 2: n * 4, 3: n * 4, 4: n * 4, 5: n * 4, 6: n * 4, 7: n * 4, 8: n * 4,
                              9: n * 4, 10: n * 16}
        self.card_count = 0

    def remaining_cards(self):
        cards = []
        for card, count in self.card_contents.items():
            cards.extend([card] * count)
        return cards

    def hit_card(self):
        remaining = self.remaining_cards()
        if not remaining:
            return None
        card = random.choice(remaining)
        if card in ['A', 10]:
            self.card_count -= 1
        elif card in [2, 3, 4, 5, 6]:
            self.card_count += 1
        self.card_contents[card] -= 1
        return str(card)

    def reset_deck(self):
        self.card_contents = {'A': self.n * 4, 2: self.n * 4, 3: self.n * 4, 4: self.n * 4, 5: self.n * 4,
                              6: self.n * 4, 7: self.n * 4, 8: self.n * 4, 9: self.n * 4, 10: self.n * 16}
        self.card_count = 0

    def get_len(self):
        return sum(self.card_contents.values())

class game:
    def __init__(self, betting_strategy, blackjack_strategy, number_decks=6, reset_deck=4, nb_iter=1000,
                 counting_cards=True):
        self.mydeck = n_decks(number_decks)
        self.blackjack_strategy = blackjack_strategy
        self.betting_strategy = betting_strategy
        self.number_decks = number_decks
        self.reset_deck = reset_deck
        self.nb_iter = nb_iter
        self.counting_cards = counting_cards

    def run_game(self):
        player_hand = [self.mydeck.hit_card(), self.mydeck.hit_card()]
        dealer_hand = [self.mydeck.hit_card()]

        next_move = first_hand(self.blackjack_strategy, player_hand, dealer_hand[0])

        if next_move == 1:
            while True:
                player_hand.append(self.mydeck.hit_card())
                next_move, player_sums = next_hands(self.blackjack_strategy, player_hand, dealer_hand[0])
                if next_move == 0:
                    break
                if min(player_sums) > 21:
                    return -1

        player_sums = [i for i in sum_hand(player_hand) if i <= 21]
        if len(player_sums) == 0:
            return -1
        player_result = max(player_sums)

        if player_result > 21:
            return -1

        dealer_hand.append(self.mydeck.hit_card())

        while max(sum_hand(dealer_hand)) < 17:
            dealer_hand.append(self.mydeck.hit_card())

        dealer_sums = [i for i in sum_hand(dealer_hand) if i <= 21]
        if len(dealer_sums) == 0:
            return 1
        dealer_result = max(dealer_sums)
        if dealer_result > 21:
            return 1
        elif player_result > dealer_result:
            return 1
        elif player_result == dealer_result:
            return 0
        else:
            return -1

    def run_day(self, iters):
        counter = 0
        portfolio = 0
        negative_counter = 0
        positive_counter = 0
        all_positive = 0
        all_negative = 0
        for _ in range(iters):
            card_counting = round(self.mydeck.card_count / self.number_decks)

            if card_counting > max(self.betting_strategy.keys()):
                mise = self.betting_strategy[max(self.betting_strategy.keys())]
            elif card_counting < min(self.betting_strategy.keys()):
                mise = self.betting_strategy[min(self.betting_strategy.keys())]
            else:
                mise = self.betting_strategy[card_counting]
            result = self.run_game()
            portfolio += mise * result
            counter += result
            if card_counting < 0:
                all_negative += 1
                negative_counter += max(0, result)
            elif card_counting > 0:
                all_positive += 1
                positive_counter += max(0, result)
            # print(portfolio, mise, result, round(self.mydeck.card_count/self.number_decks))
            if self.mydeck.get_len() <= self.reset_deck * 52 + 20:
                self.mydeck.reset_deck()
        print(positive_counter / all_positive, negative_counter / all_negative)
        print(portfolio)
        return counter, portfolio

    def optimize_betting_strategy(self, learning_rate=0.1, iterations=100):
        best_portfolio = float('-inf')
        best_strategy = self.betting_strategy.copy()

        for iteration in range(iterations):
            for key in self.betting_strategy.keys():
                original_bet = self.betting_strategy[key]

                # Try increasing the bet
                self.betting_strategy[key] += learning_rate
                _, portfolio = self.run_day(self.nb_iter)
                if portfolio > best_portfolio:
                    best_portfolio = portfolio
                    best_strategy = self.betting_strategy.copy()
                else:
                    # Try decreasing the bet
                    self.betting_strategy[key] -= 2 * learning_rate
                    _, portfolio = self.run_day(self.nb_iter)
                    if portfolio > best_portfolio:
                        best_portfolio = portfolio
                        best_strategy = self.betting_strategy.copy()
                    else:
                        # Revert to original bet if no improvement
                        self.betting_strategy[key] = original_bet

            print(f"Iteration {iteration + 1}: Best Portfolio = {best_portfolio}")

        self.betting_strategy = best_strategy