"""
Test module for skills.
"""

from nose.tools import assert_equals
from dmaid.model.fifth.skills import SkillsMixin
from dmaid.model.fifth.ability_scores import AbilityScoresMixin


class TestSkillsMixin(object):

    def setup(self):

        test_skills_dict = {
            'athletics': 0,
            'arcana': 2,
        }
        test_proficiency_dict = {
            'athletics': False,
            'arcana': True,
            'investigation': False,
        }
        test_ability_dict = {
            'str_num': 10,
            'int_num': 14
        }
        self.proficiency = 2
        self.skills = SkillsMixin(test_skills_dict, test_proficiency_dict, test_ability_dict)

    def test_skill_mod_generated_correctly_when_not_proficient(self):

        expected_athletics_mod = 0
        expected_investigation_mod = 2

        assert_equals(self.skills.skill_mod('athletics', proficiency=self.proficiency), expected_athletics_mod)
        assert_equals(self.skills.skill_mod('investigation', proficiency=self.proficiency), expected_investigation_mod)

    def test_skill_mod_generated_correctly_when_proficient(self):

        expected_arcana_mod = 6

        assert_equals(self.skills.skill_mod('arcana', proficiency=self.proficiency), expected_arcana_mod)

