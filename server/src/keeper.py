from fluxx import Card


class Keeper(Card):
    """docstring for Keeper"""
    def __init__(self, name):
        super(Keeper, self).__init__(name)
        self.category = 'keeper'

    def play(self, game, playerNumber):
        super(Keeper, self).play(game, playerNumber)
        p = game.players[playerNumber]
        p.deck.add(self)


class Creeper(Keeper):
    """docstring for Creeper"""
    def __init__(self, name):
        super(Creeper, self).__init__(name)
        self.category = 'creeper'


class Creeper1(Creeper):
    """docstring for Creeper1"""
    def __init__(self):
        super(Creeper1, self).__init__('Creeper 1')


class Creeper2(Creeper):
    """docstring for Creeper2"""
    def __init__(self):
        super(Creeper2, self).__init__('Creeper 2')


class Creeper3(Creeper):
    """docstring for Creeper3"""
    def __init__(self):
        super(Creeper3, self).__init__('Creeper 3')


class Creeper4(Creeper):
    """docstring for Creeper4"""
    def __init__(self):
        super(Creeper4, self).__init__('Creeper 4')


def allKeepers():
    result = [Creeper1(), Creeper2(), Creeper3(), Creeper4()] 
    result += [Keeper('Keeper %s' % i) for i in range(0, 23)]
    return result
