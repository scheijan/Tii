import random
import sys

from cards import Card

from keeper import *
from goals import *
from rules import *


class Game(object):
    """docstring for Game"""
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

        self.rules = []

        self.initStack()

        for player in self.players:
            player.draw(3)

    def drawFromStack(self, count=1):
        if len(self.stack) < count:
            self.restock()
        return self.stack.draw(count)

    def discard(self, card):
        self.discard.add(card)

    def setGoal(self, goal):
        print('new goal: %s' % goal)
        self.goal = goal

    def addRule(self, rule):
        print('new rule: %s' % rule)
        self.rules.append(rule)

    def initStack(self):
        allCards = []
        allCards += allGoals()
        allCards += allRules()
        allCards += allKeepers()
        for card in allCards:
            self.stack.add(card)

        self.stack.shuffle()

    def restock(self):
        self.stack.add(self.discard._cards)
        self.discard = Stack()
        self.stack.shuffle()

    def printGameState(self):
        print(50 * ' *')
        print('game state')
        print(50 * ' *')
        print('players: ')
        for player in self.players:
            print(player)

        print('round: %s' % self.round)
        print('current goal: %s' % self.goal)
        print('number of cards on the main stack: %s' % len(self.stack))
        print('number of cards on the discard stack: %s' % len(self.discard))
        print('number of rules: %s' % len(self.rules))
        print('cards to draw per round: %s' % self.cardsToDraw)
        print('cards to play per round: %s' % self.cardsToPlay)
        print('hand limit: %s' % self.handLimit)
        print('keeper limit: %s' % self.keeperLimit)
        print(50 * ' *')


class Player(object):
    """docstring for Player"""
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
        if len(self.hand) > 0:
            c = self.hand.remove(card)
            c.play(self.game, self.number)

    def draw(self, count=1):
        drawn = self.game.drawFromStack(count)
        for c in drawn:
            if c.category == 'creeper':
                c.play(self.game, self.number)
                self.draw()

        drawn = [c for c in drawn if c.category != 'creeper']
        # print('Player %s draws card(s): %s' % (self.number, drawn))
        self.hand.add(drawn)

    def hasCreeper(self):
        result = False
        for c in self.deck:
            if c.category == 'creeper':
                result = True
        return result

    def hasKeeper(self, name):
        result = False
        for c in self.deck:
            if c.name == name:
                result = True
        return result

    def turn(self):
        self.draw(self.game.cardsToDraw)
        for i in range(0, self.game.cardsToPlay):
            self.play(0)
        self.endTurn()

    def endTurn(self):
        won = True
        if not self.game.goal or self.hasCreeper():
            won = False
        else:
            for condition in self.game.goal.conditions:
                if not self.hasKeeper(condition):
                    won = False

        if won:
            print(self.game.printGameState())
            print(50 * ' *')
            print('Player %s won!!!' % self.number)
            print(50 * ' *')

            sys.exit()

        else:
            if self.number == self.game.numberOfPlayers - 1:
                self.game.round += 1


class Stack(object):
    """docstring for Stack"""
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
        random.shuffle(self._cards)

    def draw(self, count=1):
        if len(self._cards) == 0:
            return []
        elif len(self._cards) < count:
            count = len(self._cards)
        drawn = self._cards[0:count]
        del self._cards[0:count]
        return drawn

    def add(self, cards):
        if isinstance(cards, list):
            self._cards += cards
        else:
            self._cards.append(cards)

    def remove(self, card):
        result = self._cards[card]
        del self._cards[card]
        return result

    def setLimit(self, limit):
        self._limit = limit

    def getLimit(self):
        return self._limit


if __name__ == '__main__':
    game = Game()

    p1 = game.players[0]
    p2 = game.players[1]

    game.printGameState()
    for i in range(0, 10):
        p1.turn()
        p2.turn()
    game.printGameState()
