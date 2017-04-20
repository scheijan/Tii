from tii import *


class Rule(Card):
    """base class for rules, implements a generic version of the 'play' method"""

    def __init__(self, name):
        super(Rule, self).__init__(name)
        self.category = 'rule'
        self.name = name

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Card and adds the rule to the game"""
        super(Rule, self).play(game, playerNumber)
        game.addRule(self)


class HandLimit1(Rule):
    """rule, sets the hand limit to 1 when played"""

    def __init__(self):
        super(HandLimit1, self).__init__('Hand Limit 1')

    def play(self, game, playerNumber):
        super(HandLimit1, self).play(game, playerNumber)
        game.handLimit = 1
        self.id = 'R1'


class HandLimit2(Rule):
    """rule, sets the hand limit to 2 when played"""

    def __init__(self):
        super(HandLimit2, self).__init__('Hand Limit 2')

    def play(self, game, playerNumber):
        super(HandLimit2, self).play(game, playerNumber)
        game.handLimit = 2
        self.id = 'R2'


class HandLimit3(Rule):
    """rule, sets the hand limit to 3 when played"""

    def __init__(self):
        super(HandLimit3, self).__init__('Hand Limit 3')

    def play(self, game, playerNumber):
        super(HandLimit3, self).play(game, playerNumber)
        game.handLimit = 3
        self.id = 'R3'


class HandLimit4(Rule):
    """rule, sets the hand limit to 4 when played"""

    def __init__(self):
        super(HandLimit4, self).__init__('Hand Limit 4')

    def play(self, game, playerNumber):
        super(HandLimit4, self).play(game, playerNumber)
        game.handLimit = 4
        self.id = 'R4'


class KeeperLimit4(Rule):
    """rule, sets the keeper limit to 4 when played"""

    def __init__(self):
        super(KeeperLimit4, self).__init__('Keeper Limit 4')

    def play(self, game, playerNumber):
        super(KeeperLimit4, self).play(game, playerNumber)
        game.keeperLimit = 4
        self.id = 'R5'


class Play2(Rule):
    """rule, sets 'play cards per round' to 2 when played"""

    def __init__(self):
        super(Play2, self).__init__('Play 2')

    def play(self, game, playerNumber):
        super(Play2, self).play(game, playerNumber)
        game.cardsToPlay = 2
        self.id = 'R6'


class Play3(Rule):
    """rule, sets 'play cards per round' to 3 when played"""

    def __init__(self):
        super(Play3, self).__init__('Play 3')

    def play(self, game, playerNumber):
        super(Play3, self).play(game, playerNumber)
        game.cardsToPlay = 3
        self.id = 'R7'


class Play4(Rule):
    """rule, sets 'play cards per round' to 4 when played"""

    def __init__(self):
        super(Play4, self).__init__('Play 4')

    def play(self, game, playerNumber):
        super(Play4, self).play(game, playerNumber)
        game.cardsToPlay = 4
        self.id = 'R8'


class Draw2(Rule):
    """rule, sets 'draw cards per round' to 2 when played"""

    def __init__(self):
        super(Draw2, self).__init__('Draw 2')

    def play(self, game, playerNumber):
        super(Draw2, self).play(game, playerNumber)
        game.cardsToDraw = 2
        self.id = 'R9'


class Draw3(Rule):
    """rule, sets 'draw cards per round' to 3 when played"""

    def __init__(self):
        super(Draw3, self).__init__('Draw 3')

    def play(self, game, playerNumber):
        super(Draw3, self).play(game, playerNumber)
        game.cardsToDraw = 3
        self.id = 'R10'


class Draw4(Rule):
    """rule, sets 'draw cards per round' to 4 when played"""

    def __init__(self):
        super(Draw4, self).__init__('Draw 4')

    def play(self, game, playerNumber):
        super(Draw4, self).play(game, playerNumber)
        game.cardsToDraw = 4
        self.id = 'R11'


class Draw5(Rule):
    """rule, sets 'draw cards per round' to 5 when played"""

    def __init__(self):
        super(Draw5, self).__init__('Draw 5')

    def play(self, game, playerNumber):
        super(Draw5, self).play(game, playerNumber)
        game.cardsToDraw = 5
        self.id = 'R12'


def allRules():
    return [HandLimit1(), HandLimit2(), HandLimit3(), HandLimit4(), KeeperLimit4(), Play2(), Play3(), Play4(), Draw2(), Draw3(), Draw4(), Draw5()]
