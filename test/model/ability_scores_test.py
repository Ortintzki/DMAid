"""
Unit tests for ability scores.
"""

from nose.tools import assert_equals
from dmaid.model.fifth.ability_scores import AbilityScores

class TestAbilityScores(object):

    def setup(self):

        self.abilities = AbilityScores()

    def test_strmod(self):
        self.abilities.strength = 10
        assert_equals(0, self.abilities.strmod)

    def test_dexmod(self):
        self.abilities.dexterity = 10
        assert_equals(0, self.abilities.dexmod)

    def test_conmod(self):
        self.abilities.constitution = 10
        assert_equals(0, self.abilities.conmod)

    def test_intmod(self):
        self.abilities.intelligence = 10
        assert_equals(0, self.abilities.intmod)

    def test_wismod(self):
        self.abilities.wisdom = 10
        assert_equals(0, self.abilities.wismod)

    def test_chamod(self):
        self.abilities.charisma = 10
        assert_equals(0, self.abilities.chamod)
