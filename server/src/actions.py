import logging

from cards import Card
from stack import Stack


class Action(Card):
    """base class for actions, child classes NEED to implement a special version of the 'play' method"""

    def __init__(self, name):
        super(Action, self).__init__(name)
        self.category = 'action'
        self.name = name

    def play(self, game, playerNumber):
        super(Action, self).play(game, playerNumber)
        game.discard.add(self)


class Jackpot(Action):
    """Jackpot: draw three cards"""

    def __init__(self):
        super(Jackpot, self).__init__('Jackpot')
        self.id = 'jackpot'
        self.description = 'Draw 3 cards'

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Action and draws 3 cards for the player"""
        super(Jackpot, self).play(game, playerNumber)
        # draw 3 cards which should not be added to the "drawnCards" counter for this round
        game.players[playerNumber].draw(3, False)


class RulesReset(Action):
    """Jackpot: reset all rules"""

    def __init__(self):
        super(RulesReset, self).__init__('Rules Reset')
        self.id = 'rulesreset'
        self.description = 'Reset to the Basic Rules'

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Action and resets all rules"""
        super(RulesReset, self).play(game, playerNumber)
        # move all cards from the rules stack to the discard stack
        numberOfRules = len(game.rules)
        if numberOfRules > 0:
            for i in range(numberOfRules - 1, -1, -1):
                rule = game.rules.remove(i)
                game.discard.add(rule)

            # reset to the basic rule limits
            game.cardsToDraw = 1
            game.cardsToPlay = 1
            game.keeperLimit = -1
            game.handLimit = -1


class DiscardAndDraw(Action):
    """DiscardAndDraw: discard all hand cards and draw new ones"""

    def __init__(self):
        super(DiscardAndDraw, self).__init__('Discard and Draw')
        self.id = 'discardanddraw'
        self.description = 'Discard your entire hand, then draw as many cards as you discarded'

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Action, discards all hand cards and draws an equal amount of new cards"""
        super(DiscardAndDraw, self).play(game, playerNumber)

        player = game.players[playerNumber]
        numberOfCards = len(player.hand)
        if numberOfCards > 0:
            # discard all card on hand
            for i in range(numberOfCards - 1, -1, -1):
                card = player.hand.remove(i)
                game.discard.add(card)
            # draw new cards
            for i in range(0, numberOfCards):
                player.draw()


class JamesBaxter(Action):
    """Jame Baxter: All players draw a card, all keeper/hand limits are discarded"""

    def __init__(self):
        super(JamesBaxter, self).__init__('James Baxter')
        self.id = 'jamesbaxter'
        self.description = 'All players draw a card. All Hand and Keeper Limits are discarded.'

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Action, draws a card for all players and removes all keeper/hand limits"""
        super(JamesBaxter, self).play(game, playerNumber)

        # loop over all players and draw one card each
        for player in game.players:
            player.draw()

        # remove all hand/keeper limit cards and add them to the discard stack
        removedCards = game.rules.removeRulesByType('hand')
        removedCards += game.rules.removeRulesByType('keeper')

        for card in removedCards:
            game.discard.add(card)

        # reset limits
        game.handLimit = -1
        game.keeperLimit = -1


class MixItAllUp(Action):
    """Jame Baxter: All players draw a card, all keeper/hand limits are discarded"""

    def __init__(self):
        super(MixItAllUp, self).__init__('Mix It All Up')
        self.id = 'mixitallup'
        self.description = 'Gather up all the Keepers on the table, shuffle them together and deal them back out'

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Action, draws a card for all players and removes all keeper/hand limits"""
        super(MixItAllUp, self).play(game, playerNumber)

        # loop over all players and collect the keepers in their fields in a new stack
        allKeepers = Stack()
        for player in game.players:
            if len(player.field) > 0:
                for i in range(len(player.field) - 1, -1, -1):
                    card = player.field.remove(i)
                    allKeepers.add(card)

        # shuffle
        allKeepers.shuffle()

        # while there are keepers distribute them to players, starting with the current player
        i = playerNumber
        while len(allKeepers) > 0:
            game.players[i].field.add(allKeepers.draw())
            if i == len(game.players) - 1:
                i = 0
            else:
                i += 1


def allActions():
    return [Jackpot(), RulesReset(), DiscardAndDraw(), JamesBaxter(), MixItAllUp()]
