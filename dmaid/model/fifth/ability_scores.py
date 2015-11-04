"""
Module to handle ability score operations, derivations.
"""

class AbilityScores(object):
    """
    Class object for ability scores and such.
    """

    def __init__(self, str_num=0, dex_num=0, con_num=0, int_num=0, wis_num=0, cha_num=0):

        self.strength = int(str_num)
        self.dexterity = int(dex_num)
        self.constitution = int(con_num)
        self.intelligence = int(int_num)
        self.wisdom = int(wis_num)
        self.charisma = int(cha_num)

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
