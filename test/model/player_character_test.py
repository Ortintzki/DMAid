"""
Unit tests for player character behaviour.
"""

from nose.tools import assert_equals
from dmaid.model.fifth.player_character import Character


class TestPlayerCharacter(object):

    def setup(self):

        ability_kwargs = {
            'str_num': 10
        }
        personality_kwargs = {}
        descriptive_kwargs = {}
        self.test_character = Character(ability_kwargs, personality_kwargs, descriptive_kwargs)

    def test_mixins_properly_created_and_accessible(self):

        assert_equals(self.test_character.strength, 10)
