"""
Unit tests for ability scores.
"""

from nose.tools import assert_equals
from dmaid.model.fifth.ability_scores import AbilityScoresMixin


class TestAbilityScores(object):

    def setup(self):

        self.abilities = AbilityScoresMixin(strength=10, dexterity=12, str_save=True)

    def test_mod(self):

        assert_equals(self.abilities.ability_mod('strength'), 0)
        assert_equals(self.abilities.ability_mod('dexterity'), 1)

    def test_saving_throws(self):

        expected_str_save = 2
        expected_dex_save = 1
        proficiency = 2

        assert_equals(self.abilities.saving_throw_mod('strength', proficiency=proficiency), expected_str_save)
        assert_equals(self.abilities.saving_throw_mod('dexterity', proficiency=proficiency), expected_dex_save)
