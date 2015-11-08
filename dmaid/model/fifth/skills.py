"""
Skill check module
"""
from dmaid.model.fifth.ability_scores import AbilityScoresMixin


class SkillsMixin(AbilityScoresMixin, object):
    """
    Skills and skill check handler.
    """

    SKILL_MAPPING = {
        'acrobatics': 'dexterity',
        'animal_handling': 'charisma',
        'arcana': 'intelligence',
        'athletics': 'strength',
        'deception': 'charisma',
        'history': 'intelligence',
        'intimidation': 'charisma',
        'insight': 'wisdom',
        'investigation': 'intelligence',
        'medicine': 'wisdom',
        'nature': 'intelligence',
        'perception': 'wisdom',
        'performance': 'charisma',
        'persuasion': 'charisma',
        'religion': 'intelligence',
        'sleight_of_hand': 'dexterity',
        'stealth': 'dexterity',
        'survival': 'wisdom',
    }

    def __init__(self, skill_value_dict, skill_proficiency_dict, ability_kwarg_dict):
        """

        :param skill_value_dict: a dictionary of integers representing the base skill value keyed to the skill name
        :param skill_proficiency_dict: a dictionary of booleans indicating if the character is proficient in the skill
        :param ability_kwarg_dict: a dictionary of kwargs to initialize AbilityScoresMixin with
        :return:
        """

        AbilityScoresMixin.__init__(self, **ability_kwarg_dict)
        self.acrobatics = skill_value_dict.get('acrobatics', 0)
        self.animal_handling = skill_value_dict.get('animal_handling', 0)
        self.arcana = skill_value_dict.get('arcana', 0)
        self.athletics = skill_value_dict.get('athletics', 0)
        self.deception = skill_value_dict.get('deception', 0)
        self.history = skill_value_dict.get('history', 0)
        self.intimidation = skill_value_dict.get('intimidation', 0)
        self.insight = skill_value_dict.get('insight', 0)
        self.investigation = skill_value_dict.get('investigation', 0)
        self.medicine = skill_value_dict.get('medicine', 0)
        self.nature = skill_value_dict.get('nature', 0)
        self.perception = skill_value_dict.get('perception', 0)
        self.performance = skill_value_dict.get('performance', 0)
        self.persuasion = skill_value_dict.get('persuasion', 0)
        self.religion = skill_value_dict.get('religion', 0)
        self.sleight_of_hand = skill_value_dict.get('sleight_of_hand', 0)
        self.stealth = skill_value_dict.get('stealth', 0)
        self.survival = skill_value_dict.get('survival', 0)

        self.proficiency_dict = skill_proficiency_dict

    def skill_mod(self, skill, proficiency=0):

        proficiency_value = 0 if not self.proficiency_dict[skill] else proficiency
        return self.__getattribute__(skill) + proficiency_value + self.ability_mod(self.SKILL_MAPPING[skill])
