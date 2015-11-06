"""
Unit tests for descriptive traits.
"""

from nose.tools import assert_equals
from dmaid.model.fifth.descriptive_traits import Descriptions


class TestDescriptions(object):

    def setup(self):

        self.descriptions = Descriptions()
        self.descriptions.classes = {
            'fighter': 2,
            'wizard': 1,
        }

    def test_char_level(self):

        expected = 3
        actual = self.descriptions.char_level
        assert_equals(expected, actual)
