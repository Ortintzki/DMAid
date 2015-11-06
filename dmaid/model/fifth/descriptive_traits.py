"""
Model for the generally cosmetic or rarely referenced traits.
Includes class because once you derive class abilities you basically never use it.
"""
import logging


class DescriptionsMixin(object):
    """
    Descriptions model.
    """
    def __init__(self, char_name="", player_name="", classes=None, race='', alignment=None, background="", age=0,
                 height=(0, 0), weight=0, eyes="", skin="", hair=""):

        super(DescriptionsMixin, self).__init__()

        # Core character attributes
        self.char_name = char_name
        self.player_name = player_name
        self.classes = Classes(classes)
        self.race = race
        self.alignment = alignment
        self.background = background

        # Superficial traits
        self.age = age
        self.height = height
        self.weight = weight
        self.eyes = eyes
        self.skin = skin
        self.hair = hair

    @property
    def char_level(self):
        """
        Return total level possessed by the character.
        """
        return self.classes.char_level()


class Alignments(object):
    """
    Alignment constants.
    """
    # pylint: disable=C0103, W0612
    LG = "Lawful Good"
    LN = "Lawful Neutral"
    LE = "Lawful Evil"
    NG = "Neutral Good"
    N = "Neutral"
    NE = "Neutral Evil"
    CG = "Chaotic Good"
    CN = "Chaotic Neutral"
    CE = "Chaotic Evil"


class Classes(object):
    """

    """

    def __init__(self, classes_dict):

        for _, level in classes_dict.iteritems():
            if not type(level) is int:
                logging.error("Classes object only supports integer values, got type %s", type(level))
                raise ValueError

        self.classes_dict = classes_dict

    def char_level(self):
        value = 0
        for _, level in self.classes_dict.iteritems():
            value += level
        return value