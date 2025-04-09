import random

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        if self.rank == 'A':
            return 1
        elif self.rank == 'J':
            return 10
        elif self.rank == 'Q':
            return 15
        elif self.rank == 'K':
            return 20
        else:
            return int(self.rank)

    def get_life(self):
        if self.rank == 'J':
            return 20
        elif self.rank == 'Q':
            return 30
        elif self.rank == 'K':
            return 40

class Game:
    def __init__(self):
        self.tavern = []
        self.castle = []
        self.hand = []
        self.cemetery = []
        self.board = []
        self.play = []
        self.alive = True
        self.jester = 2
        # Set up the game
        self.create_castle()
        self.create_tavern()
        self.draw_card(8)

    def create_castle(self):
        jacks = []
        queens = []
        kings = []
        for suit in suits:
            jacks.append(('J',suit))
            queens.append(('Q',suit))
            kings.append(('K',suit))
        random.shuffle(jacks)
        random.shuffle(queens)
        random.shuffle(kings)
        self.castle = jacks + queens + kings

    def create_tavern(self):
        for suit in suits:
            for rank in ranks[:-3]:
                self.tavern.append((rank,suit))
        random.shuffle(self.tavern)

    def draw_card(self,num):
        for i in range(num):
            if len(self.tavern) == 0:
                print('Tavern is empty')
                break
            elif len(self.hand) == 8:
                print('Your hand has been filled')
                input()
                break
            else:
                card = self.tavern.pop()
                self.hand.append(card)

    # Auxiliary functions for the turn functions
    
    def print_cards_in_list(self,list):
        for card in list:
            print(f'{card[0]} {card[1]}')

    def print_hand(self):
        print('The cards in your hand are:')
        self.print_cards_in_list(self.hand)

    def print_top_castle(self):
        print(f'{self.castle[0][0]} {self.castle[0][1]}')

    def print_tavern_cemetery(self):
        print(f'The number of cards in the tavern is {len(self.tavern)}')
        print(f'The number of cards in the discard pile is {len(self.cemetery)}')
        if len(self.cemetery) > 0:
            print(f'The top card of the cemetery is {self.cemetery[-1][0]} {self.cemetery[-1][1]}')

    def print_board(self):
        print('The cards on the board are:')
        for card in self.board:
            print(f'{card[0]} {card[1]}')

    def show_board_state(self):
        print('=======================================================')
        print(f'The royal in top of the castle is:')
        self.print_top_castle()
        if self.board != []:
            print('\n')
            print('Your current board is:')
            for list in self.board:
                self.print_cards_in_list(list)
        print('\n')
        self.print_tavern_cemetery()
        print('\n')

    def solve_hearts(self,num):
        if self.castle[0][1] != 'hearts':
            for i in range(num):
                if len(self.cemetery) == 0:
                    print('The discard pile was emptied')
                    input()
                    break
                else:
                    random.shuffle(self.cemetery)
                    card = self.cemetery.pop()
                    self.tavern.insert(0, card)
        else:
            print('Suit countered by the royal')
            input()

    def solve_suit(self):
        if len(self.play) == 1:
            card = self.play[0]
            if card[1] == 'diamonds':
                if self.castle[0][1] != 'diamonds':
                    card = Card(card[0], card[1])
                    self.draw_card(card.get_value())
                else:
                    print('Suit countered by the royal')
                    input()
            elif card[1] == 'hearts':
                card = Card(card[0], card[1])
                self.solve_hearts(card.get_value())
        elif len(self.play) == 2:
            if self.play[0][0] == 'A' and self.play[0][1] == self.play[1][1]:
                card = Card(self.play[1][0],self.play[1][1])
                if card.get_suit() == 'diamonds':
                    if self.castle[0][1] != 'diamonds':
                        self.draw_card(card.get_value() + 1)
                    else:
                        print('Suit countered by the royal')
                        input()
                elif card.get_suit() == 'hearts':
                    self.solve_hearts(card.get_value() + 1)
            else:
                total_value = 0
                for card in self.play:
                    card = Card(card[0], card[1])
                    total_value += card.get_value()
                for card in self.play:
                    card = (total_value, card[1])
                    if card[1] == 'diamonds':
                        if self.castle[0][1] != 'diamonds':
                            card = Card(card[0], card[1])
                            self.draw_card(card.get_value())
                        else:
                            print('Suit countered by the royal')
                            input()
                    elif card[1] == 'hearts':
                        card = Card(card[0], card[1])
                        self.solve_hearts(card.get_value())
        else:
            total_value = 0
            for card in self.play:
                card = Card(card[0], card[1])
                total_value += card.get_value()
            for card in self.play:
                card = (total_value, card[1])
                if card[1] == 'diamonds':
                    if self.castle[0][1] != 'diamonds':
                        card = Card(card[0], card[1])
                        self.draw_card(card.get_value())
                    else:
                        print('Suit countered by the royal')
                        input()
                elif card[1] == 'hearts':
                    card = Card(card[0], card[1])
                    self.solve_hearts(card.get_value())

    def check_ace(self,card):
        if len(self.play) < 2:
            if card[0] == 'A':
                a = input('Do you want to play another card? (y/n): ')
                if a == 'y':
                    card = input('Choose a card to play: ')
                    card = card.split()
                    card = (card[0], card[1])
                    if card not in self.hand:
                        print('Card not in hand')
                        self.play_ace()            
                    self.hand.remove(card)
                    self.play.append(card)
                elif a == 'n':
                    pass
                else:
                    print('Invalid input')
                    self.check_ace(card)
        else:
            pass

    def check_combo(self, card):
        if card[0] == 'A' or card[0] == '2' or card[0] == '3' or card[0] == '4' or card[0] == '5':
            total_value = 0
            if card[0] == 'A':
                total_value += 1
            else:
                total_value += int(card[0])
            while True:
                found = False
                for other_card in self.hand:
                    if card[0] == other_card[0]:
                        if other_card[0] == 'A':
                            next_value = 1
                        else:
                            next_value = int(other_card[0])
                        if total_value + next_value > 10:
                            break 
                        a = input(f'You can play {other_card[0]} {other_card[1]}, wanna play it? (y/n): ')
                        print('\n')
                        if a == 'y':
                            self.hand.remove(other_card)
                            self.play.append(other_card)
                            total_value += next_value
                            found = True
                            break 
                        elif a == 'n':
                            continue
                        else:
                            print('Invalid input')
                if not found:
                    break
        else:
            pass

    def clean_board(self):
        for list in self.board:
            for card in list:
                self.cemetery.append(card)
        self.board = []

    def get_board_damage(self):
        damage = 0
        royal = self.castle[0]
        if royal[1] != 'clubs':
            for list in self.board:
                if len(list) == 1:
                    card = list[0]
                    card = Card(card[0],card[1])
                    if card.get_suit() != 'clubs':
                        damage += card.get_value()
                    else:
                        damage += card.get_value() * 2
                else:
                    total_value = 0
                    clubs = False
                    for card in list:
                        card = Card(card[0],card[1])
                        if card.get_suit() == 'clubs':
                            clubs = True
                        total_value += card.get_value()
                    if clubs == True:
                        damage += total_value * 2
                    else:
                        damage += total_value
        else:
            warning = False
            for list in self.board:
                for card in list:
                    card = Card(card[0],card[1])
                    damage += card.get_value()
                    if card.get_suit() == 'clubs':
                        warning = True
            if warning == True:
                print("Cards of clubs won't double damage.")
        return damage
    
    def get_royal_damage(self):
        royal_damage = 0
        royal = self.castle[0]
        royal = Card(royal[0],royal[1])
        royal_damage = royal.get_value()
        if royal.get_suit() != 'spades':
            for list in self.board:
                if len(list) == 1:
                    card = list[0]
                    card = Card(card[0],card[1])
                    if card.get_suit() == 'spades':
                        royal_damage -= card.get_value()
                else:
                    total_value = 0
                    spades = False
                    for card in list:
                        card = Card(card[0],card[1])
                        if card.get_suit() == 'spades':
                            spades = True
                        total_value += card.get_value()
                    if spades == True:
                        royal_damage -= total_value
        else:
            warning = False
            for list in self.board:
                for card in list:
                    if card[1] == 'spades':
                        warning = True
            if warning == True:
                print("Cards of spades won't reduce damage.")
        return royal_damage
    
    def discard(self, num):
        discard_value = 0
        discard = []
        if self.jester > 0:
            self.print_hand()
            print('\n')
            a = input('You may use a jester now, if you want to, wanna use it? (y/n): ')
            if a == 'y':
                self.jester -= 1
                self.solve_jester()
                self.discard(num)
            elif a == 'n':
                print('\n')
                while len(self.hand) > 0 and discard_value < num:
                    print('=======================================================')
                    print(f'Your current discard is {discard_value}. You have to discard at least {num - discard_value} more in card value.')
                    print('\n')
                    self.print_hand()
                    print('\n')
                    card = input('Choose a card to discard: ')
                    card = card.split()
                    if len(card) != 2: 
                        print('Invalid card format. Please enter a valid card (e.g., "9 spades").')
                        continue
                    card = (card[0], card[1])
                    if card not in self.hand:
                        print('Card not in hand')
                        continue
                    print('\n')
                    self.hand.remove(card)
                    discard.append(card)
                    card = Card(card[0], card[1])
                    discard_value += card.get_value()
                if len(self.hand) == 0 and discard_value < num:
                    print("You ran out of cards and you could not survive the hit.")
                    self.alive = False
                else:
                    print('You survived, next turn.')
                for card in discard:
                    self.cemetery.append(card)
            else:
                print('Choose a valid answer.')
                self.discard(num)
        else:
            print('\n')
            while len(self.hand) > 0 and discard_value < num:
                print('=======================================================')
                print(f'Your current discard is {discard_value}. You have to discard at least {num - discard_value} more in card value.')
                print('\n')
                self.print_hand()
                print('\n')
                card = input('Choose a card to discard: ')
                card = card.split()
                if len(card) != 2: 
                    print('Invalid card format. Please enter a valid card (e.g., "9 spades").')
                    continue
                card = (card[0], card[1])
                if card not in self.hand:
                    print('Card not in hand')
                    continue
                print('\n')
                self.hand.remove(card)
                discard.append(card)
                card = Card(card[0], card[1])
                discard_value += card.get_value()
            if len(self.hand) == 0 and discard_value < num:
                self.alive = False
            else:
                print('You survived, next turn.')
            for card in discard:
                self.cemetery.append(card)

    def take_damage(self):
        royal_damage = self.get_royal_damage()
        print(f'Prepare for the hit from the royal. You will take {royal_damage} damage.')
        input()
        self.discard(royal_damage)
        input()

    def solve_jester(self):
        for card in self.hand:
            self.cemetery.append(card)
        self.hand = []
        self.draw_card(8)

    # Turn functions

    def play_card(self):
        self.show_board_state()
        if len(self.hand) == 0:
            if self.jester > 0:
                a = input('Your hand is empity, wanna use a jester? (y/n): ')
                if a == 'y':
                    self.jester -= 1
                    self.solve_jester()
                    self.play_card()
                else:
                    print('You ran out of cards without cleaning the castle.')
                    self.alive = False
            else:
                print('You ran out of cards without cleaning the castle.')
                self.alive = False
        else:
            self.print_hand()
            print('\n')
            card = input('Choose a card to play: ')
            print('=======================================================')
            if card == 'jester':
                if self.jester > 0:
                    self.jester -= 1
                    self.solve_jester()
                    self.play_card()
                else:
                    print('There are no jesters left.') 
                    self.play_card()
            elif card == 'yield':
                print('You choose to yield')
                print('\n')
                print('=======================================================')
                return
            card = card.split()
            if len(card) != 2:
                print('Invalid card format. Please enter a valid card (e.g., "9 spades").')
                self.play_card()
                return
            card = (card[0], card[1])
            if card not in self.hand:
                print('Card not in hand')
                self.play_card()          
            else:
                self.hand.remove(card)
                self.play.append(card)
                self.check_combo(card)
                self.check_ace(card)
                self.board.append(self.play)
                self.solve_suit()
                print('Your play is:')
                for card in self.play:
                    print(f'{card[0]} {card[1]}')
                print("Let's check if royal is dead.")
                input()
                print('=======================================================')
                self.play = []

    def check_royal_death(self):
        royal = self.castle[0]
        royal = Card(royal[0],royal[1])
        print('The royal is:')
        self.print_top_castle()
        print('\n')
        print('Your actual board is:')
        for list in self.board:
            self.print_cards_in_list(list)
        print('\n')
        damage = self.get_board_damage()
        if damage == royal.get_life():
            print('You killed royal with damage equal to its life. Royal moved to top tavern.')
            royal_defeated = self.castle.pop(0)
            self.tavern.append(royal_defeated)
            self.clean_board()
            input()
        elif damage > royal.get_life():
            print('You killed royal with damage greater than its life. Royal moved to discard pile.')
            royal_defeated = self.castle.pop(0)
            self.cemetery.append(royal_defeated)
            self.clean_board()
            input()
        else:
            print(f'Royal still alive. Your current damage is {damage}.')
            input()
            print('=======================================================')
            self.take_damage()