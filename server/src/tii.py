import random
import sys

from cards import Card

from keeper import *
from goals import *
from rules import *


class Game(object):
    """main game object for Tii"""

    def __init__(self, numberOfPlayers=2):
        super(Game, self).__init__()
        self.stack = Stack()
        self.discard = Stack()
        self.numberOfPlayers = numberOfPlayers
        self.players = []
        for i in range(0, numberOfPlayers):
            self.players.append(Player(i, self))
        self.goal = None
        self.handLimit = -1
        self.keeperLimit = -1
        self.cardsToDraw = 1
        self.cardsToPlay = 1
        self.round = 0
        self.won = False
        self.winner = None

        self.rules = []

        self.initStack()

        for player in self.players:
            player.draw(3)

    def drawFromStack(self, count=1):
        """draw a card from the stack and return it, restock if necessary"""
        if len(self.stack) < count:
            self.restock()
        return self.stack.draw(count)

    def discard(self, card):
        """discard a single card and add it to the discard stack"""
        self.discard.add(card)

    def setGoal(self, goal):
        """set the game's goal to the passed goal card"""
        # check win conditions here?
        print('new goal: %s' % goal)
        self.goal = goal

    def addRule(self, rule):
        """add the passed rule card to the list of current rules"""
        # remove obsolete rules and discard them
        print('new rule: %s' % rule)
        self.rules.append(rule)

    def initStack(self):
        """initialize a standard deck of cards and shuffle them"""
        allCards = []
        allCards += allGoals()
        allCards += allRules()
        allCards += allKeepers()
        for card in allCards:
            self.stack.add(card)

        self.stack.shuffle()

    def restock(self):
        """use the discard stack and possible leftover cards from the stack and reshuffle"""
        self.stack.add(self.discard._cards)
        self.discard = Stack()
        self.stack.shuffle()

    def gameState(self):
        """print the current state of the game, for debugging purposes"""
        result = 50 * ' *'
        result += '\ngame state\n'
        result += 50 * ' *'
        result += '\nplayers: \n'
        for player in self.players:
            result += str(player)
            result += '\n'

        result += 'round: %s\n' % self.round
        result += 'current goal: %s\n' % self.goal
        result += 'number of cards on the main stack: %s\n' % len(self.stack)
        result += 'number of cards on the discard stack: %s\n' % len(self.discard)
        result += 'number of rules: %s\n' % len(self.rules)
        result += 'cards to draw per round: %s\n' % self.cardsToDraw
        result += 'cards to play per round: %s\n' % self.cardsToPlay
        result += 'hand limit: %s\n' % self.handLimit
        result += 'keeper limit: %s\n' % self.keeperLimit
        if self.won:
            result += 50 * ' *'
            result += '\n'
            result += '%s won the game!!\n' % self.winner

        result += 50 * ' *'
        return result


class Player(object):
    """base class for a player with name, number and empty stacks for their hand and deck"""

    def __init__(self, number, game):
        super(Player, self).__init__()
        self.number = number
        self.name = 'Player %s' % number

        self.game = game
        self.hand = Stack()

        self.deck = Stack()

    def __repr__(self):
        return '%s: %s / %s' % (self.name, self.hand, self.deck)

    def play(self, card):
        """remove the passed card from the player's hand and play it"""
        if len(self.hand) > 0:
            c = self.hand.remove(card)
            c.play(self.game, self.number)

    def draw(self, count=1):
        """draw a card from the stack, repeat until it's not a creeper"""
        drawn = self.game.drawFromStack(count)
        for c in drawn:
            if c.category == 'creeper':
                c.play(self.game, self.number)
                self.draw()

        drawn = [c for c in drawn if c.category != 'creeper']
        # print('Player %s draws card(s): %s' % (self.number, drawn))
        self.hand.add(drawn)

    def hasCreeper(self):
        """check player's deck for creepers"""
        result = False
        for c in self.deck:
            if c.category == 'creeper':
                result = True
        return result

    def hasKeeper(self, name):
        """check whether the player has a certain keeper/creeper"""
        result = False
        for c in self.deck:
            if c.name == name:
                result = True
        return result

    def turn(self):
        """simulate a player's turn: draw cards and play the first card on hand"""
        self.draw(self.game.cardsToDraw)
        for i in range(0, self.game.cardsToPlay):
            self.play(0)
        return self.endTurn()

    def endTurn(self):
        """ends a turn and checks for win conditions, increases the turn counter"""
        won = True
        if not self.game.goal or self.hasCreeper():
            won = False
        else:
            for condition in self.game.goal.conditions:
                if not self.hasKeeper(condition):
                    won = False

        if won:
            self.game.won = True
            self.game.winner = self
            print(self.game.gameState())

        else:
            if self.number == self.game.numberOfPlayers - 1:
                self.game.round += 1
        return won


class Stack(object):
    """base class for a stack of cards"""

    def __init__(self):
        super(Stack, self).__init__()
        self._cards = []
        self._limit = -1

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return '%s (limit %s)' % (self._cards, self._limit)

    def __iter__(self):
        return iter(self._cards)

    def shuffle(self):
        """shuffle the deck of cards"""
        random.shuffle(self._cards)

    def draw(self, count=1):
        """draw a card from the deck if possible"""
        if len(self._cards) == 0:
            return []
        elif len(self._cards) < count:
            count = len(self._cards)
        drawn = self._cards[0:count]
        del self._cards[0:count]
        return drawn

    def add(self, cards):
        """add one or more cards to the stack"""
        if isinstance(cards, list):
            self._cards += cards
        else:
            self._cards.append(cards)

    def remove(self, card):
        """remove a card from the deck"""
        result = self._cards[card]
        del self._cards[card]
        return result

    def setLimit(self, limit):
        """set the limit of the stack"""
        self._limit = limit

    def getLimit(self):
        """get the limit of the stack"""
        return self._limit


if __name__ == '__main__':
    game = Game()

    p1 = game.players[0]
    p2 = game.players[1]

    print(game.gameState())
    for i in range(0, 10):
        p1.turn()
        p2.turn()
    print(game.gameState())
