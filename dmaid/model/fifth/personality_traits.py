"""
Model for a character's personality traits.
"""
class Personality(object):
    """
    Stored in key-value pairs in which the key is a short name for the trait,
    and the value is a full descriptor of the trait.
    """
    # Roleplaying traits

    def __init__(self, personality="", ideals="", bonds="", flaws=""):
        """
        Init
        """
        self.personality = personality
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws

