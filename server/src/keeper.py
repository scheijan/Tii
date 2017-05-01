from cards import Card


class Keeper(Card):
    """base class for keepers, implements a generic version of the 'play' method"""
    def __init__(self, name, id, types=[]):
        super(Keeper, self).__init__(name)
        self.category = 'keeper'
        self.id = id
        # keepers should be able to have 0-2 types for special wind conditons (candy / princess)
        self.types = types

    def play(self, game, playerNumber):
        """add the keeper to the player's field"""
        # needs check for keeper limit?
        super(Keeper, self).play(game, playerNumber)
        p = game.players[playerNumber]
        p.field.add(self)


KEEPERS = ['batterfly', 'butterfly', 'chicken', 'crab', 'fox', 'piggy', 'salmon', 'sloth', 'fancy-pick', 'focusing-orb', 'grand-ol-grinder', 'quill',
           'tincturing-kit', 'beer', 'crabato-juice', 'hooch', 'snail', 'string', 'firefly', 'sparkly', 'dark-patch', 'patch', 'paper', 'peat']


def allKeepers():
    result = [Keeper(k, k) for k in KEEPERS]
    return result
