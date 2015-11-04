"""
Model for the generally cosmetic or rarely referenced traits.
Includes class because once you derive class abilities you basically never use it.
"""
class Descriptions(object):
    """
    Descriptions model.
    """
    def __init__(self, char_name="", player_name="", classes=None, race='', alignment=None, background="", age=0,
                 height=(0, 0), weight=0, eyes="", skin="", hair=""):

        # Core character attributes
        self.char_name = char_name
        self.player_name = player_name
        self.classes = classes
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
        level = 0
        for _, value in self.classes.items():
            level += value
        return level


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

