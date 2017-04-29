import random


class Stack(object):
    """base class for a stack of cards"""

    def __init__(self):
        super(Stack, self).__init__()
        self._cards = []
        self._limit = -1

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        # return '%s (limit %s)' % (self._cards, self._limit)
        return str([str(foo) for foo in self._cards])

    def __iter__(self):
        return iter(self._cards)

    def shuffle(self):
        """shuffle the deck of cards"""
        random.shuffle(self._cards)

    def draw(self, count=1):
        """draw a card from the stack if possible"""
        if len(self._cards) == 0:
            return []
        elif len(self._cards) < count:
            count = len(self._cards)
        drawn = self._cards[0:count]
        del self._cards[0:count]
        return drawn

    def add(self, cards):
        """add one or more cards to the stack"""
        if isinstance(cards, list):
            self._cards += cards
        else:
            self._cards.append(cards)

    def remove(self, card):
        """remove a card from the stack"""
        result = self._cards[card]
        del self._cards[card]
        return result

    def setLimit(self, limit):
        """set the limit of the stack"""
        self._limit = limit

    def getLimit(self):
        """get the limit of the stack"""
        return self._limit

    def hasCard(self, cardID):
        """check for a specific card in this stack"""
        for card in self._cards:
            if card.id == cardID:
                return True
        return False


class RulesStack(Stack):
    """special stack for rules, only allows one card per type, removes cards automatically as necessary"""

    def add(self, cards):
        """adds rules to the stack and removes all rules with the same types"""
        if not isinstance(cards, list):
            cards = [cards]
        for newCard in cards:
            self._cards = [card for card in self._cards if not card.type == newCard.type]

        super(RulesStack, self).add(cards)
