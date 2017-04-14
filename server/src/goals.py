from tii import *


class Goal(Card):
    """base class for goals, implements a generic version of the 'play' method"""

    def __init__(self, name):
        super(Goal, self).__init__(name)
        self.category = 'goal'
        self.description = 'a goal'
        self.conditions = []

    def __repr__(self):
        return '%s (%s) - %s' % (self.name, self.category, self.conditions)

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Card and adds the goal to the game"""
        super(Goal, self).play(game, playerNumber)
        game.setGoal(self)

    def check(self, game, playerNumber):
        pass


# dummy classes for goals
class Goal1(Goal):
    """docstring for Goal1"""

    def __init__(self):
        super(Goal1, self).__init__('Goal 1')
        self.description = 'To win you need Keeper 1 and Keeper 2.'
        self.conditions = ['Keeper 1', 'Keeper 2']


class Goal2(Goal):
    """docstring for Goal2"""

    def __init__(self):
        super(Goal2, self).__init__('Goal 2')
        self.description = 'To win you need Keeper 3 and Keeper 4.'
        self.conditions = ['Keeper 3', 'Keeper 4']


class Goal3(Goal):
    """docstring for Goal3"""

    def __init__(self):
        super(Goal3, self).__init__('Goal 3')
        self.description = 'To win you need Keeper 5 and Keeper 6.'
        self.conditions = ['Keeper 5', 'Keeper 6']


class Goal4(Goal):
    """docstring for Goal4"""

    def __init__(self):
        super(Goal4, self).__init__('Goal 4')
        self.description = 'To win you need Keeper 7 and Keeper 8.'
        self.conditions = ['Keeper 7', 'Keeper 8']


class Goal5(Goal):
    """docstring for Goal5"""

    def __init__(self):
        super(Goal5, self).__init__('Goal 5')
        self.description = 'To win you need Keeper 9 and Keeper 10.'
        self.conditions = ['Keeper 9', 'Keeper 10']


def allGoals():
    return [Goal1(), Goal2(), Goal3(), Goal4(), Goal5()]
