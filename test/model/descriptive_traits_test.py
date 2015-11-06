"""
Unit tests for descriptive traits.
"""

from nose.tools import assert_equals
from dmaid.model.fifth.descriptive_traits import DescriptionsMixin, Classes


class TestDescriptions(object):

    def setup(self):

        self.descriptions = DescriptionsMixin(classes={'fighter': 2, 'wizard': 1})

    def test_char_level(self):

        expected = 3
        actual = self.descriptions.char_level
        assert_equals(expected, actual)

