#!/usr/bin/env python
# coding: utf-8


# Awa Konate IS_211
import random
import argparse
import sys
import time

"""Main function instantiates players"""


class Players():
    """ A constructor for Players."""

    def __init__(self):
        self.roll = True
        self.hold = False
        self.turn = False
        self.score = 0

    def choice(self):
        """A function for playing and/or passing."""
        decide = str(raw_input('To Roll (r) or Hold (h)? '))
        if decide == 'r':
            self.roll = True
            self.hold = False
        elif decide == 'h':
            self.roll = False
            self.hold = True
        else:
            print('Invalid Entry. To Roll (r) or Hold (h)? ')
            self.choice()


"""Main function instantiates players"""


class ComputerPlayer(Players):
    """A strategy constructor for PC Players."""

    def pc_choice(self):
        min_val = 25
        max_val = 100 - self.score
        if min_val < max_val:
            limit = min_val
        else:
            limit = max_val

        if self.score_turn < limit:
            print('Player is on roll')
            self.hold = False
            self.roll = True
        else:
            print('Player is on hold')
            self.hold = True
            self.roll = False


"""determines what type of player"""


def correctplayer(player_type):
    """Determines who is playing."""

    if player_type == 'I am HUMAN':
        return Players()
    elif player_type == ' I am COMPUTER':
        return ComputerPlayer()
    else:
        print('ERROR: Unknown Player')


class PlayerFactory():
    """A constructor for the correct player type."""


"""Game class executes the game"""


class Game():
    """Constructor for a two player game called Pig Game."""

    def __init__(self, player1, player2, dice):
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player1.name = 'PLAYER 1'
        self.player2.name = 'PLAYER 2'
        self.dice = dice
        self.score_turn = 0
        """random flip"""
        flip = random.randint(1, 2)
        if flip == 1:
            """determines if player 1 will go first"""
            self.cur_player = player1
            print('Coin flip PLAYER 1 will begin.')
        elif flip == 2:
            """determines if player 2 will go first"""
            self.cur_player = player2
            print('Coin flip PLAYER 2 will begin.')
        else:
            print('Error, please try again.')
        self.player_turn()

    def next_turn(self):
        """Players next turn at rolling & total scores and will continue until a score of 100 is reached"""
        self.score_turn = 0
        if self.player1.score >= 100:
            print('Player 1 WON! The score is: '), self.player1.score
            sys.exit()
            newGame()
        elif self.player2.score >= 100:
            print('Player 2 WON! The score is: '), self.player2.score
            sys.exit()
            newGame()
        else:
            """switching players"""
            if self.cur_player == self.player1:
                self.cur_player = self.player2
            elif self.cur_player == self.player2:
                self.cur_player = self.player1
            else:
                print('Error, please try again.')
        print(self.cur_player.name, 'WILL NOW PLAY.')
        self.player_turn()

    def player_turn(self):
        """A players turn at rolling."""
        print('The total score for Player 1: '), self.player1.score
        print('The total score for Player 2: '), self.player2.score
        self.dice.roll()
        if self.dice.val == 1:
            print('Rolled ''1'', No points earned, and you lost, next turn')
            self.turn_score = 0
            """Switch player"""
            self.next_turn()
        else:
            self.score_turn = self.score_turn + self.dice.val
            print('You rolled a number: '), self.dice.val
            print('You score this turn is: '), self.score_turn
            self.cur_player.choice()
            if self.cur_player.hold == True and self.cur_player.roll == False:
                self.cur_player.score = self.cur_player.score + self.score_turn
                """Adds the total score"""
                self.next_turn()
            elif self.cur_player.hold == False and self.cur_player.roll == True:
                self.player_turn()


"""timed aspect: the game will continue until either someone scores 100, or one minute has elapsed since the start of the game."""


class TimedGameProxy(Game):
    """Docstring."""

    def __init__(self):
        self.start = time.time()
        Game.__init__(self, player1='PLAYER1', player2='PLAYER2')

    def time_check(self):
        """Docstring"""
        start = raw_input('Do you want to play a new timed aspect game? Y/N ')
        if start == 'Y' or 'y':
            player1 = Players()
            player2 = Players()
            dice = Dice()
            new = Game(player1, player2, dice)
        elif start == 'N' or 'n':
            print('Bye!')

        if time.time() - self.start >= 60:
            print('GAME OVER')
        elif self.player1.score > self.player2.score:
            print('Player 1 WON!. Total score is: '), self.player1.score
        else:
            if self.player2.score > self.player1.score:
                print('Player 2 WON!. Total score is: '), self.player2.score
            sys.exit()

    def next_turn(self):
        """Players next turn at rolling & total scores."""
        self.score_turn = 0
        if self.player1.score >= 100:
            print('Player 1 WON!. The score is: '), self.player1.score
            sys.exit()
            newGame()
        elif self.player2.score >= 100:
            print('Player 2 WON!. The score is: '), self.player2.score
            sys.exit()
            newGame()
        else:
            if self.cur_player == self.player1:
                self.cur_player = self.player2
            elif self.cur_player == self.player2:
                self.cur_player = self.player1
            else:
                print('Error!!')
        print(self.cur_player.name, 'WILL PLAY.')
        self.player_turn()

    def player_turn(self):
        """A players turn at rolling."""
        print('The total score for Player 1: '), self.player1.score
        print('The total score for Player 2: '), self.player2.score
        self.dice.roll()
        if self.dice.val == 1:
            print('Rolled ''1'', No points earned, & you lost your turn')
            self.turn_score = 0
            self.next_turn()
        else:
            self.score_turn = self.score_turn + self.dice.val
            print('Rolled a number: '), self.dice.val
            print('You score this turn is: '), self.score_turn
            self.cur_player.choice()
            if self.cur_player.hold == True and self.cur_player.roll == False:
                self.cur_player.score = self.cur_player.score + self.score_turn
                self.next_turn()
            elif self.cur_player.hold == False and self.cur_player.roll == True:
                self.player_turn()

    def times_up(self):
        """Docstring."""
        if self.player1.score > self.player2.score:
            print('Time is up, PLAYER 1 wins!')
            sys.exit()

        elif self.player2.score > self.player1.score:
            print('Time is up, PLAYER 2 wins!')
            sys.exit()

        else:
            print('TIED, no body wins!')
            sys.exit()


"""Method executes the 'turn' by rolling """


class Dice():
    """ A constructor for Dice. and sets a random seed for consistency"""

    def __init__(self):
        self.val = int()
        seed = 0

    def roll(self):
        """A random roll between 1-6."""
        self.val = random.randint(1, 6)


def newGame():
    """A function for playing or exiting the game and combined instructions and new game"""
    print('\nWelcome to the PIG DICE GAME')
    print('-----------------------------''\n')
    print('How to Play: 2 Players Only')
    print(' ''\n')
    print('Each turn, a player can roll the dice  to accumulate points. ')
    print('Any number rolled between 2-6 counts towards the total score. ')
    print('If a "1" is rolled points and turn is lost. Each player can choose. ')
    print('to roll or hold at any time unless a "1" is rolled; which at that')
    print('the moment you lose your turn and points.')
    print('The player who reaches 100 points WINS!')
    print(' ''\n')

    start = raw_input('Do you want to play? Y/N ')
    if start == 'Y'.lower():
        player1 = Players()
        player2 = Players()
        dice = Dice()
        new = Game(player1, player2, dice)
    elif start == 'N'.lower():
        print('Good bye!')
        sys.exit()
    else:
        print('Invalid entry, please try again. Enter ''y'' or ''n''')
        newGame()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--player1', help='State whether human or computer')
    parser.add_argument('--player2', help='Stat whether human or computer')
    parser.add_argument('--timed', help='Game is timed for 1 minute')
    args = parser.parse_args()

    if args.timed:
        time_game = TimedGameProxy()
    else:
        no_time_game = newGame()

    # if __name__ == '__main__':
    main()
