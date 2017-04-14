class Card(object):
    """docstring for Card"""
    def __init__(self, name):
        super(Card, self).__init__()
        self.name = name
        self.category = 'card'

    def __repr__(self):
        return '%s (%s)' % (self.name, self.category)

    def play(self, game, playerNumber):
        print('Player %s plays card: %s' % (playerNumber, self))
