from cards import Card


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
        self.description = 'Draw 3 cards!'

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Action (Card) and draws 3 cards for the player"""
        super(Jackpot, self).play(game, playerNumber)
        # draw 3 cards which should not be added to the "drawnCards" counter for this round
        game.players[playerNumber].draw(3, False)


def allActions():
    return [Jackpot()]
