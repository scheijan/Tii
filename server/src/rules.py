from fluxx import *

class Rule(Card):
    """docstring for Rule"""
    def __init__(self, name):
        super(Rule, self).__init__(name)
        self.category = 'rule'
        self.name = name

    def play(self, game, playerNumber):
        super(Rule, self).play(game, playerNumber)
        game.addRule(self)


class HandLimit1(Rule):
    """docstring for HandLimit1"""
    def __init__(self):
        super(HandLimit1, self).__init__('Hand Limit 1')

    def play(self, game, playerNumber):
        super(HandLimit1, self).play(game, playerNumber)
        game.handLimit = 1


class HandLimit2(Rule):
    """docstring for HandLimit2"""
    def __init__(self):
        super(HandLimit2, self).__init__('Hand Limit 2')

    def play(self, game, playerNumber):
        super(HandLimit2, self).play(game, playerNumber)
        game.handLimit = 2


class HandLimit3(Rule):
    """docstring for HandLimit3"""
    def __init__(self):
        super(HandLimit3, self).__init__('Hand Limit 3')

    def play(self, game, playerNumber):
        super(HandLimit3, self).play(game, playerNumber)
        game.handLimit = 3


class HandLimit4(Rule):
    """docstring for HandLimit4"""
    def __init__(self):
        super(HandLimit4, self).__init__('Hand Limit 4')

    def play(self, game, playerNumber):
        super(HandLimit4, self).play(game, playerNumber)
        game.handLimit = 4


class KeeperLimit4(Rule):
    """docstring for KeeperLimit4"""
    def __init__(self):
        super(KeeperLimit4, self).__init__('Keeper Limit 4')

    def play(self, game, playerNumber):
        super(KeeperLimit4, self).play(game, playerNumber)
        game.keeperLimit = 4


class Play2(Rule):
    """docstring for Play2"""
    def __init__(self):
        super(Play2, self).__init__('Play 2')

    def play(self, game, playerNumber):
        super(Play2, self).play(game, playerNumber)
        game.cardsToPlay = 2


class Play3(Rule):
    """docstring for Play3"""
    def __init__(self):
        super(Play3, self).__init__('Play 3')

    def play(self, game, playerNumber):
        super(Play3, self).play(game, playerNumber)
        game.cardsToPlay = 3


class Play4(Rule):
    """docstring for Play4"""
    def __init__(self):
        super(Play4, self).__init__('Play 4')

    def play(self, game, playerNumber):
        super(Play4, self).play(game, playerNumber)
        game.cardsToPlay = 4


class Draw2(Rule):
    """docstring for Draw2"""
    def __init__(self):
        super(Draw2, self).__init__('Draw 2')

    def play(self, game, playerNumber):
        super(Draw2, self).play(game, playerNumber)
        game.cardsToDraw = 2


class Draw3(Rule):
    """docstring for Draw3"""
    def __init__(self):
        super(Draw3, self).__init__('Draw 3')

    def play(self, game, playerNumber):
        super(Draw3, self).play(game, playerNumber)
        game.cardsToDraw = 3


class Draw4(Rule):
    """docstring for Draw4"""
    def __init__(self):
        super(Draw4, self).__init__('Draw 4')

    def play(self, game, playerNumber):
        super(Draw4, self).play(game, playerNumber)
        game.cardsToDraw = 4


class Draw5(Rule):
    """docstring for Draw5"""
    def __init__(self):
        super(Draw5, self).__init__('Draw 5')

    def play(self, game, playerNumber):
        super(Draw5, self).play(game, playerNumber)
        game.cardsToDraw = 5

def allRules():
    return [HandLimit1(), HandLimit2(), HandLimit3(), HandLimit4(), KeeperLimit4(), Play2(), Play3(), Play4(), Draw2(), Draw3(), Draw4(), Draw5()]
