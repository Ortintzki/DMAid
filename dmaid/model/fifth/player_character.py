"""
Model for a player character in DnD 5e
"""
from dmaid.model.fifth.ability_scores import AbilityScoresMixin
from dmaid.model.fifth.personality_traits import PersonalityMixin
from dmaid.model.fifth.descriptive_traits import DescriptionsMixin


class Character(AbilityScoresMixin, PersonalityMixin, DescriptionsMixin, object):
    """
    Character model.

    Refer to the appropriate mixins for how the dictionaries should be structured.
    """
    # pylint: disable=W0142
    def __init__(self, ability_kwargs, personality_kwargs, description_kwargs, proficiency=2, hp=0, ac=10, initiative=0,
                 speed=0):

        AbilityScoresMixin.__init__(self, **ability_kwargs)
        PersonalityMixin.__init__(self, **personality_kwargs)
        DescriptionsMixin.__init__(self, **description_kwargs)

        # Skills
        # are probably just a list of skills that the character is proficient
        # in, which is used to compute the actual score.  It's just ability
        # mod and proficiency anyway.

        # Mechanical scores
        self.inspiration = False
        self.proficiency = proficiency
        self.hit_points = hp
        self.armor_class = ac
        self.initiative = initiative
        self.speed = speed

    def saving_throw(self, ability):
        return AbilityScoresMixin._saving_throw(self, self.proficiency, ability)