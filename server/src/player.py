import logging

from stack import *


class Player(object):
    """base class for a player with name, number and empty stacks for their hand and field"""

    def __init__(self, number, game):
        super(Player, self).__init__()
        self.number = number
        self.name = 'Player %s' % number

        self.game = game
        self.hand = Stack()

        self.field = Stack()

        self.cardsPlayed = 0
        self.cardsDrawn = 0

    def __repr__(self):
        return '%s: %s / %s' % (self.name, self.hand, self.field)

    def play(self, card):
        """remove the passed card from the player's hand and play it"""
        if len(self.hand) > 0:
            c = self.hand.remove(card)
            c.play(self.game, self.number)
            self.cardsPlayed += 1

    def draw(self, count=1, countAsDraw=True):
        """draw a card from the stack, repeat until it's not a creeper"""
        drawn = self.game.drawFromStack(count)
        for c in drawn:
            if c.category == 'creeper':
                c.play(self.game, self.number)
                self.draw()

        drawn = [c for c in drawn if c.category != 'creeper']
        # print('Player %s draws card(s): %s' % (self.number, drawn))
        self.hand.add(drawn)
        if countAsDraw:
            self.cardsDrawn += len(drawn)
        logging.info("%s draws %s card(s)" % (self.name, self.cardsDrawn))

    def hasCreeper(self):
        """check player's field for creepers"""
        result = False
        for c in self.field:
            if 'creeper' in c.types:
                result = True
        return result

    def hasKeeper(self, name):
        """check whether the player has a certain keeper/creeper"""
        result = False
        for c in self.field:
            if c.name == name:
                result = True
        return result

    def turn(self):
        """simulate a player's turn: draw cards and play the first card on hand"""
        logging.info("Player %s begins" % self.number)
        self.cardsDrawn = 0
        self.cardsPlayed = 0
        while not self.obeysDrawLimit():
            self.draw(1)
        while not self.obeysPlayLimit() and not self.game.won:
            self.play(0)
            while not self.obeysDrawLimit():
                self.draw(1)
        while not self.obeysHandLimit() and not self.game.won:
            card = self.hand.remove(0)
            self.game.discardCard(card)
        while not self.obeysKeeperLimit() and not self.game.won:
            card = self.field.remove(0)
            self.game.discardCard(card)

        if self.canEndTurn():
            return self.endTurn()
        else:
            logging.error("can't end turn")

    def obeysHandLimit(self):
        """ensure player obeys hand limit"""
        logging.debug("hand limit: %s (hand: %s)" % (self.game.handLimit, len(self.hand)))
        return self.game.handLimit >= len(self.hand) or self.game.handLimit == -1

    def obeysKeeperLimit(self):
        """ensure player obeys keeper limit"""
        logging.debug("keeper limit: %s (keepers out: %s)" % (self.game.keeperLimit, len(self.field)))
        return self.game.keeperLimit >= len(self.field) or self.game.keeperLimit == -1

    def obeysDrawLimit(self):
        """ensure player draws correct number of cards"""
        logging.debug("draw limit: %s (drawn: %s)" % (self.game.cardsToDraw, self.cardsDrawn))
        return self.game.cardsToDraw <= self.cardsDrawn or len(self.game.stack) == 0

    def obeysPlayLimit(self):
        """ensure player plays correct number of cards"""
        result = False
        # if the player has 0 cards we return true
        if len(self.hand) == 0:
            result = True
        # if the rule is "Play All" and the player has not 0 cards, we return false
        elif self.game.rules.hasCard('PlayAll'):
            result = False
        # otherwise we check whether the player has player enough cards this round
        elif self.game.cardsToPlay <= self.cardsPlayed:
            result = True

        logging.debug("play limit: %s (played: %s, hand: %s)" % (self.game.cardsToPlay, self.cardsPlayed, len(self.hand)))
        return result

    def canEndTurn(self):
        """evaluates if ending a turn is allowed"""
        return self.game.won or (self.obeysHandLimit() and self.obeysKeeperLimit() and self.obeysDrawLimit() and self.obeysPlayLimit())

    def endTurn(self):
        """ends a turn and checks for win conditions, increases the turn counter"""
        won = True
        if not self.game.goal or self.hasCreeper():
            won = False
        else:
            if hasattr(self.game.goal, 'check'):
                won = self.game.goal.check(self)
            else:
                for condition in self.game.goal.conditions:
                    if not self.hasKeeper(condition):
                        won = False

        if won:
            self.game.won = True
            self.game.winner = self
            logging.info(self.game.gameState())

        else:
            if self.number == self.game.numberOfPlayers - 1:
                self.game.round += 1
                logging.info("round %s" % self.game.round)
        return won
