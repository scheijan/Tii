from copy import deepcopy

import jsonpickle

from keeper import allKeepers
from goals import allGoals
from rules import allRules
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
        self.handLimit = -1
        self.keeperLimit = -1
        self.cardsToDraw = 1
        self.cardsToPlay = 1
        self.round = 0
        self.won = False
        self.winner = None

        self.rules = RulesStack()

        self.initStack()

        for player in self.players:
            player.draw(3)

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
        print('new goal: %s' % goal)
        self.goal = goal

    def addRule(self, rule):
        """add the passed rule card to the list of current rules"""
        # remove obsolete rules and discard them
        print('new rule: %s' % rule)
        self.rules.add(rule)

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
        for p in [player for player in self.players if player.number != playerNr]:
            c.players.append({'name': p.name, 'field': p.field, 'number': p.number})

        return jsonpickle.encode(c, unpicklable=False)


if __name__ == '__main__':
    game = Game()

    p1 = game.players[0]
    p2 = game.players[1]

    print(game.gameState())
    for i in range(0, 10):
        p1.turn()
        p2.turn()
    print(game.gameState())
