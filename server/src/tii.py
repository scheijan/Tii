from copy import deepcopy
import logging

import jsonpickle

from keeper import allKeepers
from goals import allGoals
from rules import allRules
from actions import allActions
from stack import Stack, RulesStack
from player import Player


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
        self._handLimit = -1
        self._keeperLimit = -1
        self._cardsToDraw = 1
        self._cardsToPlay = 1
        self.round = 0
        self.won = False
        self.winner = None

        self.rules = RulesStack()

        self.initStack()

        for player in self.players:
            player.draw(3)

    @property
    def handLimit(self):
        if self._handLimit == -1:
            return -1
        elif self.rules.hasCard('Mathematical'):
            return self._handLimit + 1
        else:
            return self._handLimit

    @handLimit.setter
    def handLimit(self, newHandLimit):
        self._handLimit = newHandLimit

    @property
    def keeperLimit(self):
        if self._keeperLimit == -1:
            return -1
        elif self.rules.hasCard('Mathematical'):
            return self._keeperLimit + 1
        else:
            return self._keeperLimit

    @keeperLimit.setter
    def keeperLimit(self, newKeeperLimit):
        self._keeperLimit = newKeeperLimit

    @property
    def cardsToDraw(self):
        if self.rules.hasCard('Mathematical'):
            return self._cardsToDraw + 1
        else:
            return self._cardsToDraw

    @cardsToDraw.setter
    def cardsToDraw(self, newCardsToDraw):
        self._cardsToDraw = newCardsToDraw

    @property
    def cardsToPlay(self):
        if self.rules.hasCard('Mathematical'):
            return self._cardsToPlay + 1
        else:
            return self._cardsToPlay

    @cardsToPlay.setter
    def cardsToPlay(self, newCardsToPlay):
        self._cardsToPlay = newCardsToPlay

    def drawFromStack(self, count=1):
        """draw a card from the stack and return it, restock if necessary"""
        if len(self.stack) < count:
            self.restock()
        return self.stack.draw(count)

    def discardCard(self, card):
        """discard a single card and add it to the discard stack"""
        self.discard.add(card)

    def setGoal(self, goal):
        """set the game's goal to the passed goal card"""
        # check win conditions here?
        logging.info('new goal: %s' % goal)
        self.goal = goal

    def addRule(self, rule):
        """add the passed rule card to the list of current rules"""
        # remove obsolete rules and discard them
        logging.info('new rule: %s' % rule)
        self.rules.add(rule)

    def initStack(self):
        """initialize a standard deck of cards and shuffle them"""
        allCards = []
        allCards += allGoals()
        allCards += allRules()
        allCards += allKeepers()
        allCards += allActions()
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
        if self.goal:
            result += 'conditions: %s\n' % self.goal.conditions
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

    def playerState(self, playerNr):
        c = deepcopy(self)
        c.players = None
        c.stack = None
        p = self.players[playerNr]
        c.hand = p.hand
        c.field = p.field
        c.name = p.name
        c.players = []
        c.winner = None

        c.gameData = {}
        c.gameData['cardsToDraw'] = self.cardsToDraw
        c.gameData['cardsToPlay'] = self.cardsToPlay
        c.gameData['keeperLimit'] = self.keeperLimit
        c.gameData['handLimit'] = self.handLimit

        for p in [player for player in self.players if player.number != playerNr]:
            c.players.append({'name': p.name, 'field': p.field, 'number': p.number})

        return jsonpickle.encode(c, unpicklable=False)


if __name__ == '__main__':
    game = Game()

    p1 = game.players[0]
    p2 = game.players[1]

    logging.info(game.gameState())
    for i in range(0, 10):
        p1.turn()
        p2.turn()
    logging.info(game.gameState())
