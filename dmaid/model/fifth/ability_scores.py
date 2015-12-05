"""
Module to handle ability score operations, derivations.
"""


class AbilityScoresMixin(object):
    """
    Class object for ability scores and such.
    """

    SAVE_MAPPING = {
        'strength': 'str_save',
        'dexterity': 'dex_save',
        'constitution': 'con_save',
        'intelligence': 'int_save',
        'wisdom': 'wis_save',
        'charisma': 'cha_save',
    }

    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0, str_save=False,
                 dex_save=False, con_save=False, int_save=False, wis_save=False, cha_save=False):

        super(AbilityScoresMixin, self).__init__()
        self.strength = int(strength)
        self.dexterity = int(dexterity)
        self.constitution = int(constitution)
        self.intelligence = int(intelligence)
        self.wisdom = int(wisdom)
        self.charisma = int(charisma)

        self.str_save = bool(str_save)
        self.dex_save = bool(dex_save)
        self.con_save = bool(con_save)
        self.int_save = bool(int_save)
        self.wis_save = bool(wis_save)
        self.cha_save = bool(cha_save)

    def ability_mod(self, ability):
        """
        Returns the ability modifier of an ability.
        :param ability: The ability to retrieve the modifier of
        """
        return int(self.__getattribute__(ability) - 10) / 2

    def saving_throw_mod(self, ability, proficiency=0):
        """
        Returns the saving throw mod of an ability
        :param proficiency: the classes's proficiency modifier if necessary
        :param ability: the ability to get the saving throw mod of
        """
        saving_throw = self.ability_mod(ability)
        if self.__getattribute__(self.SAVE_MAPPING[ability]):
            saving_throw += proficiency
        return saving_throw
