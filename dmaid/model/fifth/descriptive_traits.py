"""
Model for the generally cosmetic or rarely referenced traits.
Includes class because once you derive class abilities you basically
never use it.
"""
class Descriptions(object):
    """
    Descriptions model.
    """
    def __init__(self):

        # Core character attributes
        char_name = ""
        player_name = ""
        classes = {}
        race = ""
        alignment = ""
        background = ""

        # Superficial traits
        age = 0
        height = (0, 0)
        weight = 0
        eyes = ""
        skin = ""
        hair = ""

    @property
    def char_level(self):
        """
        Return total level possessed by the character.
        """
        level = 0
        for k, v in self.classes.items():
            level += v
        return level


class Alignments(object):
    """
    Alignment constants.
    """

    def __init__(self):
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
