from tii import Card


class Keeper(Card):
    """base class for keepers, implements a generic version of the 'play' method"""
    def __init__(self, name, id):
        super(Keeper, self).__init__(name)
        self.category = 'keeper'
        self.id = id

    def play(self, game, playerNumber):
        """add the keeper to the player's deck"""
        # needs check for keeper limit?
        super(Keeper, self).play(game, playerNumber)
        p = game.players[playerNumber]
        p.deck.add(self)


class Creeper(Keeper):
    """base class for creepers"""
    def __init__(self, name, id):
        super(Creeper, self).__init__(name, id)
        self.category = 'creeper'


class Creeper1(Creeper):
    """docstring for Creeper1"""
    def __init__(self, id):
        super(Creeper1, self).__init__('Creeper 1', id)


class Creeper2(Creeper):
    """docstring for Creeper2"""
    def __init__(self, id):
        super(Creeper2, self).__init__('Creeper 2', id)


class Creeper3(Creeper):
    """docstring for Creeper3"""
    def __init__(self, id):
        super(Creeper3, self).__init__('Creeper 3', id)


class Creeper4(Creeper):
    """docstring for Creeper4"""
    def __init__(self, id):
        super(Creeper4, self).__init__('Creeper 4', id)


KEEPERS = ['batterfly', 'butterfly', 'chicken', 'crab', 'fox', 'piggy', 'salmon', 'sloth', 'fancy-pick', 'focusing-orb', 'grand-ol-grinder', 'quill',
           'tincturing-kit', 'beer', 'crabato-juice', 'hooch', 'snail', 'string', 'firefly', 'sparkly', 'dark-patch', 'patch', 'paper', 'peat']


def allKeepers():
    result = [Creeper1('C1'), Creeper2('C2'), Creeper3('C3'), Creeper4('C4')]
    result += [Keeper(k, k) for k in KEEPERS]
    return result
