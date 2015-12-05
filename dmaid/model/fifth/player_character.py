"""
Model for a player character in DnD 5e
"""
import logging

from dmaid.model.fifth.skills import SkillsMixin
from dmaid.model.fifth.personality_traits import PersonalityMixin
from dmaid.model.fifth.descriptive_traits import DescriptionsMixin
# from dmaid.model.fifth.ability_scores import AbilityScoresMixin


class Character(SkillsMixin, PersonalityMixin, DescriptionsMixin, object):
    """
    Character model.

    Refer to the appropriate mixins for how the dictionaries should be structured.
    """
    # pylint: disable=W0142
    def __init__(self, skill_value_dict, skill_proficiency_dict, ability_kwargs_dict, personality_kwargs,
                 description_kwargs, classes=None, inspiration=False, proficiency=2, hp=0, ac=10, speed=0):

        SkillsMixin.__init__(self, skill_value_dict, skill_proficiency_dict, ability_kwargs_dict)
        PersonalityMixin.__init__(self, **personality_kwargs)
        DescriptionsMixin.__init__(self, **description_kwargs)

        # Mechanical scores
        self.classes = Classes(classes)
        self.inspiration = bool(inspiration)
        self.proficiency = int(proficiency)
        self.hit_points = int(hp)
        self.armor_class = int(ac)
        self.initiative = self.ability_mod('dexterity')
        self.speed = int(speed)

    @property
    def char_level(self):
        """
        Return total level possessed by the character.
        """
        return self.classes.char_level()


class Classes(object):
    """
    Handles character classes

    TODO: This is going to have to get yanked out and expanded in the future.
    """

    def __init__(self, classes_dict):

        if classes_dict is None:
            self.classes_dict = classes_dict
            return

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
