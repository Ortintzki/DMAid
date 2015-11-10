"""
Model for a player character in DnD 5e
"""
from dmaid.model.fifth.skills import SkillsMixin
from dmaid.model.fifth.personality_traits import PersonalityMixin
from dmaid.model.fifth.descriptive_traits import DescriptionsMixin
from dmaid.model.fifth.ability_scores import AbilityScoresMixin


class Character(SkillsMixin, PersonalityMixin, DescriptionsMixin, object):
    """
    Character model.

    Refer to the appropriate mixins for how the dictionaries should be structured.
    """
    # pylint: disable=W0142
    def __init__(self, skill_value_dict, skill_proficiency_dict, ability_kwargs_dict, personality_kwargs, description_kwargs,
                 proficiency=2, hp=0, ac=10, speed=0):

        SkillsMixin.__init__(self, skill_value_dict, skill_proficiency_dict, ability_kwargs_dict)
        PersonalityMixin.__init__(self, **personality_kwargs)
        DescriptionsMixin.__init__(self, **description_kwargs)

        # Mechanical scores
        self.inspiration = False
        self.proficiency = proficiency
        self.hit_points = hp
        self.armor_class = ac
        self.initiative = self.ability_mod('dexterity')
        self.speed = speed

