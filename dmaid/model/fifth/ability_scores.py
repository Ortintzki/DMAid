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

    def __init__(self, str_num=0, dex_num=0, con_num=0, int_num=0, wis_num=0, cha_num=0, str_save=False, dex_save=False,
                 con_save=False, int_save=False, wis_save=False, cha_save=False):

        super(AbilityScoresMixin, self).__init__()
        self.strength = int(str_num)
        self.dexterity = int(dex_num)
        self.constitution = int(con_num)
        self.intelligence = int(int_num)
        self.wisdom = int(wis_num)
        self.charisma = int(cha_num)

        self.str_save = str_save
        self.dex_save = dex_save
        self.con_save = con_save
        self.int_save = int_save
        self.wis_save = wis_save
        self.cha_save = cha_save

    def ability_mod(self, ability):
        return int(self.__getattribute__(ability) - 10) / 2

    def _saving_throw(self, proficiency, ability):
        saving_throw = self.ability_mod(ability)
        if self.__getattribute__(self.SAVE_MAPPING[ability]):
            saving_throw += proficiency
        return saving_throw
