"""
Model for a player character in DnD 5e
"""
from dmaid.model.fifth.ability_scores import AbilityScores
from dmaid.model.fifth.personality_traits import Personality
from dmaid.model.fifth.descriptive_traits import Descriptions

class Character(object):
    """
    Character model.
    """
    def __init__(self):

        self.abilities = AbilityScores()
        self.personality = Personality()
        self.descriptions = Descriptions()

        # Skills
        # are probably just a list of skills that the character is proficient 
        # in, which is used to compute the actual score.  It's just ability 
        # score and proficiency anyway.

        # Mechanical scores
        inspiration = False
        proficiency = 0
        hit_points = 0
        armor_class = 0
        initiative = 0
        speed = 0
