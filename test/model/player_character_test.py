"""
Unit tests for player character behaviour.
"""

from nose.tools import assert_equals
from dmaid.model.fifth.player_character import Character


class TestPlayerCharacter(object):

    def setup(self):

        ability_kwargs = {
            'str_num': 10,
            'dex_num': 14,
            'str_save': True,
            'dex_save': False,
        }
        personality_kwargs = {
            'personality': "I have a personality."
        }
        descriptive_kwargs = {
            'char_name': "Test McGee"
        }

        proficiency = 2

        self.test_character = Character(ability_kwargs, personality_kwargs, descriptive_kwargs, proficiency=proficiency)

    def test_mixins_properly_created_and_accessible(self):

        expected_strength = 10
        expected_personality = "I have a personality."
        expected_char_name = "Test McGee"
        assert_equals(self.test_character.strength, expected_strength)
        assert_equals(self.test_character.personality, expected_personality)
        assert_equals(self.test_character.char_name, expected_char_name)

    def test_saving_throws(self):

        expected_str_save = 2
        expected_dex_save = 2

        assert_equals(self.test_character.saving_throw('strength'), expected_str_save)
        assert_equals(self.test_character.saving_throw('dexterity'), expected_dex_save)