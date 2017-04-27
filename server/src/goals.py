from tii import *


class Goal(Card):
    """base class for goals, implements a generic version of the 'play' method"""

    def __init__(self, name):
        super(Goal, self).__init__(name)
        self.category = 'goal'
        self.description = 'a goal'
        self.id = 'an id'
        self.conditions = []

    # def __repr__(self):
    #     return '%s (%s) - %s' % (self.name, self.category, self.conditions)

    def play(self, game, playerNumber):
        """calls the generic 'play' method of Card and adds the goal to the game"""
        super(Goal, self).play(game, playerNumber)
        game.setGoal(self)

    def check(self, game, playerNumber):
        pass


class Alph(Goal):
    """docstring for Alph"""
    def __init__(self):
        super(Alph, self).__init__('Alph')
        self.description = 'Alph is the giant responsible for creating "things". And also "stuff". Approaching everything with the question "What IF?", Alph is never happier than when the answer results in a complex wadjamacallit or a satisfyingly big boom.'
        self.conditions = []
        self.id = 'alph'


class AlphSymbol(Goal):
    """docstring for Alph Symbol"""
    def __init__(self):
        super(AlphSymbol, self).__init__('Alph Symbol')
        self.description = 'Alph is the giant responsible for creating "things". And also "stuff". Approaching everything with the question "What IF?", Alph is never happier than when the answer results in a complex wadjamacallit or a satisfyingly big boom.'
        self.conditions = []
        self.id = 'alph_symbol'


class Cosma(Goal):
    """docstring for Cosma"""
    def __init__(self):
        super(Cosma, self).__init__('Cosma')
        self.description = 'As flighty and aimless as anything can be (if that thing is also giant-sized), Cosma is the Giant in charge of imagining up all things airborne. From the heaviest gas to cling to a cavern floor to the tiniest fart to escape from a butterfly, Cosma is the source of it all.'
        self.conditions = []
        self.id = 'cosma'


class CosmaSymbol(Goal):
    """docstring for CosmaSymbol"""
    def __init__(self):
        super(CosmaSymbol, self).__init__('Cosma Symbol')
        self.description = 'As flighty and aimless as anything can be (if that thing is also giant-sized), Cosma is the Giant in charge of imagining up all things airborne. From the heaviest gas to cling to a cavern floor to the tiniest fart to escape from a butterfly, Cosma is the source of it all.'
        self.conditions = []
        self.id = 'cosma_symbol'


class Friendly(Goal):
    """docstring for Friendly"""
    def __init__(self):
        super(Friendly, self).__init__('Friendly')
        self.description = 'Friendly is the overseer of darkness, nocturnal things, party-planning, of social activities and their most common lubricant, booze. Friendly by name, friendly by nature: unless you neglect to buy a round.'
        self.conditions = []
        self.id = 'friendly'


class FriendlySymbol(Goal):
    """docstring for Friendly Symbol"""
    def __init__(self):
        super(FriendlySymbol, self).__init__('Friendly Symbol')
        self.description = 'Friendly is the overseer of darkness, nocturnal things, party-planning, of social activities and their most common lubricant, booze. Friendly by name, friendly by nature: unless you neglect to buy a round.'
        self.conditions = []
        self.id = 'friendly_symbol'


class Grendaline(Goal):
    """docstring for Grendaline"""
    def __init__(self):
        super(Grendaline, self).__init__('Grendaline')
        self.description = 'Grendaline, raised in a swamp, has an imagination as free-flowing as water. This makes sense, as water is what she spends most of her time imagining. If it sprinkles, drips, flows or gushes, Grendaline is your giant.'
        self.conditions = []
        self.id = 'grendaline'


class GrendalineSymbol(Goal):
    """docstring for Grendaline Symbol"""
    def __init__(self):
        super(GrendalineSymbol, self).__init__('Grendaline Symbol')
        self.description = 'Grendaline, raised in a swamp, has an imagination as free-flowing as water. This makes sense, as water is what she spends most of her time imagining. If it sprinkles, drips, flows or gushes, Grendaline is your giant.'
        self.conditions = []
        self.id = 'grendaline_symbol'


class Humbaba(Goal):
    """docstring for Humbaba"""
    def __init__(self):
        super(Humbaba, self).__init__('Humbaba')
        self.description = 'Humbaba is the giant ruling over all creatures that walk, crawl, slither or sashay over Ur. One with the animals, Humbaba walks on all fours to be closer to them, and insists on them calling her by her first name. Which is kind of pointless, since she only has one name.'
        self.conditions = []
        self.id = 'humbaba'


class HumbabaSymbol(Goal):
    """docstring for Humbaba Symbol"""
    def __init__(self):
        super(HumbabaSymbol, self).__init__('Humbaba Symbol')
        self.description = 'Humbaba is the giant ruling over all creatures that walk, crawl, slither or sashay over Ur. One with the animals, Humbaba walks on all fours to be closer to them, and insists on them calling her by her first name. Which is kind of pointless, since she only has one name.'
        self.conditions = []
        self.id = 'humbaba_symbol'


class Lem(Goal):
    """docstring for Lem"""
    def __init__(self):
        super(Lem, self).__init__('Lem')
        self.description = 'Lem, the wanderer giant. Responsible for travel, directions, and knowledge. What Lem doesn\'t know is not worth knowing. Also, what Lem doesn\'t unknow is not worth unknowing. (That\'s Lem\'s favourite joke) (Lem doesn\'t know many jokes).'
        self.conditions = []
        self.id = 'lem'


class LemSymbol(Goal):
    """docstring for Lem Symbol"""
    def __init__(self):
        super(LemSymbol, self).__init__('Lem Symbol')
        self.description = 'Lem, the wanderer giant. Responsible for travel, directions, and knowledge. What Lem doesn\'t know is not worth knowing. Also, what Lem doesn\'t unknow is not worth unknowing. (That\'s Lem\'s favourite joke) (Lem doesn\'t know many jokes).'
        self.conditions = []
        self.id = 'lem_symbol'


class Mab(Goal):
    """docstring for Mab"""
    def __init__(self):
        super(Mab, self).__init__('Mab')
        self.description = 'When the harvest needs bringing in, the crops need counting, and the job needs doing right, Mab, Giant of Soil and Harvests, first to lie down and start imagining Ur into being is the giant to look to.'
        self.conditions = []
        self.id = 'mab'


class MabSymbol(Goal):
    """docstring for Mab Symbol"""
    def __init__(self):
        super(MabSymbol, self).__init__('Mab Symbol')
        self.description = 'When the harvest needs bringing in, the crops need counting, and the job needs doing right, Mab, Giant of Soil and Harvests, first to lie down and start imagining Ur into being is the giant to look to.'
        self.conditions = []
        self.id = 'mab_symbol'


class Pot(Goal):
    """docstring for Pot"""
    def __init__(self):
        super(Pot, self).__init__('Pot')
        self.description = 'Round of belly and capacious of stomach Pot is the Giant of Prosperity, with dominion over anything edible, cookable, munchable or nibbleworthy. Pot himself is not munchable. Do not attempt to munch any giants.'
        self.conditions = []
        self.id = 'pot'


class PotSymbol(Goal):
    """docstring for Pot Symbol"""
    def __init__(self):
        super(PotSymbol, self).__init__('Pot Symbol')
        self.description = 'Round of belly and capacious of stomach Pot is the Giant of Prosperity, with dominion over anything edible, cookable, munchable or nibbleworthy. Pot himself is not munchable. Do not attempt to munch any giants.'
        self.conditions = []
        self.id = 'pot_symbol'


class Spriggan(Goal):
    """docstring for Spriggan"""
    def __init__(self):
        super(Spriggan, self).__init__('Spriggan')
        self.description = 'Before Spriggan, no giant had ever imagined a tree. After Spriggan, no giant ever needed to, because he had already imagined them all. Steadfast, persistent, and somewhat rigid, Spriggan is the slumbering Giant of all Trees and Plants. Or "Trants".'
        self.conditions = []
        self.id = 'spriggan'


class SprigganSymbol(Goal):
    """docstring for Spriggan Symbol"""
    def __init__(self):
        super(SprigganSymbol, self).__init__('Spriggan Symbol')
        self.description = 'Before Spriggan, no giant had ever imagined a tree. After Spriggan, no giant ever needed to, because he had already imagined them all. Steadfast, persistent, and somewhat rigid, Spriggan is the slumbering Giant of all Trees and Plants. Or "Trants".'
        self.conditions = []
        self.id = 'spriggan_symbol'


class Tii(Goal):
    """docstring for Tii"""
    def __init__(self):
        super(Tii, self).__init__('Tii')
        self.description = 'The Giant with power over all numbers. Odd or even, prime or not-prime, cubed or rooted, Tii keeps a cold, watchful eye over Ur. Tii sees all, knows all, calculates all. Never underestimate Tii. Tii has already correctly estimated you.'
        self.conditions = []
        self.id = 'tii'


class TiiSymbol(Goal):
    """docstring for Tii Symbol"""
    def __init__(self):
        super(TiiSymbol, self).__init__('Tii Symbol')
        self.description = 'The Giant with power over all numbers. Odd or even, prime or not-prime, cubed or rooted, Tii keeps a cold, watchful eye over Ur. Tii sees all, knows all, calculates all. Never underestimate Tii. Tii has already correctly estimated you.'
        self.conditions = []
        self.id = 'tii_symbol'


class Zille(Goal):
    """docstring for Zille"""
    def __init__(self):
        super(Zille, self).__init__('Zille')
        self.description = 'Zille is the giant with dominion over the mountains. All rocks, caverns, hillocks, pingos, buttes and drumlins thank Zille for their existence. Zille, busy imagining up new flavours of gravel, acknowledges their thanks.'
        self.conditions = []
        self.id = 'zille'


class ZilleSymbol(Goal):
    """docstring for Zille Symbol"""
    def __init__(self):
        super(ZilleSymbol, self).__init__('Zille Symbol')
        self.description = 'Zille is the giant with dominion over the mountains. All rocks, caverns, hillocks, pingos, buttes and drumlins thank Zille for their existence. Zille, busy imagining up new flavours of gravel, acknowledges their thanks.'
        self.conditions = []
        self.id = 'zille_symbol'

class IlmenskieJones(Goal):
    """docstring for Ilmenskie Jones"""
    def __init__(self):
        super(IlmenskieJones, self).__init__('Ilmenskie Jones')
        self.description = 'some description here'
        self.conditions = []
        self.id = 'ilmenskie-jones'

class GameshowWheel(Goal):
    """docstring for Gameshow Wheel"""
    def __init__(self):
        super(GameshowWheel, self).__init__('Gameshow Wheel')
        self.description = 'some description here'
        self.conditions = []
        self.id = 'gameshow-wheel'

class MusicblockGng(Goal):
    """docstring for Musicblock GNG"""
    def __init__(self):
        super(MusicblockGng, self).__init__('Musicblock GNG')
        self.description = 'some description here'
        self.conditions = []
        self.id = 'musicblock-gng'

        


def allGoals():
    return [Alph(), AlphSymbol(), Cosma(), CosmaSymbol(), Friendly(), FriendlySymbol(), Grendaline(), GrendalineSymbol(), Humbaba(), HumbabaSymbol(), Lem(), LemSymbol(), Mab(), MabSymbol(), Pot(), PotSymbol(), Spriggan(), SprigganSymbol(), Tii(), TiiSymbol(), Zille(), ZilleSymbol(), IlmenskieJones(), GameshowWheel(), MusicblockGng()]
