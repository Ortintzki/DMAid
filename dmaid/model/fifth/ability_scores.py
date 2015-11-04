"""
Module to handle ability score operations, derivations.
"""

class AbilityScores(object):
    """
    Class object for ability scores and such.
    """

    def __init__(self):
        strength = int(0)
        dexterity = int(0)
        constitution = int(0)
        intelligence = int(0)
        wisdom = int(0)
        charisma = int(0)

    @property
    def strmod(self):
        """
        Returns strength modifier.
        """
        return int(self.strength - 10) / 2

    @property
    def dexmod(self):
        """
        Returns dexterity modifier.
        """
        return int(self.dexterity - 10) / 2

    @property
    def conmod(self):
        """
        Returns constitution modifier.
        """
        return int(self.constitution - 10) / 2

    @property
    def intmod(self):
        """
        Returns intelligence modifier.
        """
        return int(self.intelligence - 10) / 2

    @property
    def wismod(self):
        """
        Returns wisdom modifier.
        """
        return int(self.wisdom - 10) / 2

    @property
    def chamod(self):
        """
        Returns charisma modifier.
        """
        return int(self.charisma - 10) / 2
