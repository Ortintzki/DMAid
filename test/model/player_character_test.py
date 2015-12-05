"""
Unit tests for player character behaviour.
"""
import json
from nose.tools import assert_equals

from dmaid import mongo
from dmaid.model.fifth.player_character import Character

TEST_CHAR = """{
    "abilities": {
            "strength": "10",
            "dexterity": "10",
            "constitution": "10",
            "intelligence": "10",
            "wisdom": "10",
            "str_save": "false",
            "dex_save": "false",
            "con_save": "false",
            "int_save": "false",
            "wis_save": "false",
            "cha_save": "false"
    },
    "skills": {
            "acrobatics": "0",
            "animal_handling": "0",
            "arcana": "0",
            "athletics": "0",
            "deception": "0",
            "history": "0",
            "intimidation": "0",
            "insight": "0",
            "investigation": "0",
            "medicine": "0",
            "nature": "0",
            "perception": "0",
            "performance": "0",
            "persuasion": "0",
            "religion": "0",
            "sleight_of_hand": "0",
            "stealth": "0",
            "survival": "0",
            "proficiency_dict": {
                    "acrobatics": "false",
                    "animal_handling": "false",
                    "arcana": "false",
                    "athletics": "false",
                    "deception": "false",
                    "history": "false",
                    "intimidation": "false",
                    "insight": "false",
                    "investigation": "false",
                    "medicine": "false",
                    "nature": "false",
                    "perception": "false",
                    "performance": "false",
                    "persuasion": "false",
                    "religion": "false",
                    "sleight_of_hand": "false",
                    "stealth": "false",
                    "survival": "false"
            }
    },
    "inspiration": "false",
    "proficiency": "0",
    "hit_points": "0",
    "armour_class": "10",
    "speed": "0",
    "classes": {},
    "description": {
            "char_name": "Test_Char",
            "player_name": "Test_Player",
            "race": "",
            "alignment": "",
            "background": "",
            "age": "",
            "height": "",
            "weight": "",
            "eyes": "",
            "skin": "",
            "hair": ""
    },
    "personality": {
            "personality": "I have a personality",
            "ideals": "I have ideals",
            "bonds": "I have bonds",
            "flaws": "I have flaws"
    }
}"""

class TestPlayerCharacter(object):

    def setup(self):

        ability_kwargs = {
            'strength': 10,
            'dexterity': 14,
            'str_save': True,
            'dex_save': False,
        }
        personality_kwargs = {
            'personality': "I have a personality"
        }
        descriptive_kwargs = {
            'char_name': "Test McGee"
        }
        skill_value_dict = {}
        skill_proficiency_dict = {}

        proficiency = 2

        self.test_character = Character(skill_value_dict, skill_proficiency_dict, ability_kwargs, personality_kwargs,
                                        descriptive_kwargs, classes={'fighter': 2, 'wizard': 1},
                                        proficiency=proficiency)

    def test_mixins_properly_created_and_accessible(self):

        expected_strength = 10
        expected_personality = "I have a personality"
        expected_char_name = "Test McGee"
        assert_equals(self.test_character.strength, expected_strength)
        assert_equals(self.test_character.personality, expected_personality)
        assert_equals(self.test_character.char_name, expected_char_name)

    def test_char_level(self):

        expected = 3
        actual = self.test_character.char_level
        assert_equals(expected, actual)

    def test_build_char_from_json(self):

        expected_strength = 10
        expected_personality = "I have a personality"
        expected_char_name = "Test_Char"
        expected_acrobatics = 0
        expected_armour_class = 10

        test_char_from_json = json.loads(TEST_CHAR)
        test_armour_class = test_char_from_json['armour_class']
        test_abilities = test_char_from_json['abilities']
        test_description = test_char_from_json['description']
        test_personality = test_char_from_json['personality']
        test_skills = test_char_from_json['skills']

        test_character = Character(test_skills, {}, test_abilities, test_personality, test_description,
                                   ac=test_armour_class)

        assert_equals(test_character.strength, expected_strength)
        assert_equals(test_character.personality, expected_personality)
        assert_equals(test_character.char_name, expected_char_name)
        assert_equals(test_character.acrobatics, expected_acrobatics)
        assert_equals(test_character.armor_class, expected_armour_class)
