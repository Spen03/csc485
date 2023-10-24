import pytest
from csc485.projects.hw10.fruit_query import is_it_a_fruit

"""
hw14 if it returns true or false for different inputs
"""

"""
class TestHappyPath(object):
    def test_apple(self):
        assert is_it_a_fruit('apple')

    def test_pear(self):
        assert is_it_a_fruit('pear')

    def test_banana(self):
        assert is_it_a_fruit('banana')

    def test_grape(self):
        assert is_it_a_fruit('grape')
"""


# this runs through the keys______________________________
@pytest.mark.parametrize('key', [
    'apple', 'pear', 'banana', 'grape'
])
def test_good_key(key):
    # setup
    # disambiguate
    this_key = key

    # execute
    assert is_it_a_fruit(this_key)


# ______________________________________________

"""
class TestUnhappyPath(object):
    def test_not_fruit(self):
        assert not is_it_a_fruit('bingus')
"""


def test_int():
    assert not is_it_a_fruit(6)
    """
    def test_capital_banana(self):
        assert not is_it_a_fruit('Banana')

    def test_lead_space_grape(self):
        assert not is_it_a_fruit(' grape')
    """


@pytest.mark.parametrize('key', [
    'bingus', '6', 'Banana', ' grape'
])
def test_bad_key(key):
    # setup
    # disambiguate
    this_key = key

    # execute
    assert not is_it_a_fruit(this_key)


class TestNotString(object):
    def test_int(self):
        assert not is_it_a_fruit(6)
