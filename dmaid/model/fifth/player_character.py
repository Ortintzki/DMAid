"""
Model for a player character in DnD 5e
"""
from dmaid.model.fifth.ability_scores import AbilityScoresMixin
from dmaid.model.fifth.personality_traits import Personality
from dmaid.model.fifth.descriptive_traits import Descriptions


class Character(AbilityScoresMixin, object):
    """
    Character model.
    """
    # pylint: disable=W0142
    def __init__(self, ability_kwargs, personality_kwargs, description_kwargs, proficiency=2, hp=0, ac=10, initiative=0,
                 speed=0):

        super(Character, self).__init__(**ability_kwargs)
        self.personality = Personality(**personality_kwargs)
        self.descriptions = Descriptions(**description_kwargs)

        # Skills
        # are probably just a list of skills that the character is proficient
        # in, which is used to compute the actual score.  It's just ability
        # score and proficiency anyway.

        # Mechanical scores
        self.inspiration = False
        self.proficiency = proficiency
        self.hit_points = hp
        self.armor_class = ac
        self.initiative = initiative
        self.speed = speed
