import pytest

# from csc485.projects.hw11.get_fruit_name import get_formal_name
from csc485.projects.hw11.get_fruit_name_v2 import get_formal_name_v2

# can't seem to import the new file for testing. Maybe I should make a new test module?

"""
test that when the function recieves a key it knows,
it will return the correctly associated value

test that if it recieves an unknown key that it will return a key error
these keys include:
>strings
>ints 
>incorrectly formated strings
>more than one argument
>no argument
>lists
(could have tested methods but thought it unnecessary)
"""


class TestHappyPath(object):
    @pytest.mark.parametrize('good_key', [
        ('apple', 'Malus domestica'),
        ('banana', 'Musa acuminata'),
        ('orange', 'Citrus × sinensis'),
        ('strawberry', 'Fragaria × ananassa'),
        ('grape', 'Vitis vinifera'),
        ('pineapple', 'Ananas comosus'),
        ('mango', 'Mangifera indica'),
        ('blueberry', 'Vaccinium corymbosum'),
        ('peach', 'Prunus persica'),
        ('watermelon', 'Citrullus lanatus'),
        ('cherry', 'Prunus avium'),
        ('pear', 'Pyrus'),
        ('plum', 'Prunus domestica'),
        ('raspberry', 'Rubus idaeus'),
        ('kiwi', 'Actinidia deliciosa'),
        ('lemon', 'Citrus limon'),
        ('avocado', 'Persea americana'),
        ('pomegranate', 'Punica granatum'),
        ('cranberry', 'Vaccinium macrocarpon'),
        ('grapefruit', 'Citrus × paradisi')
    ])
    def test_good_key(self, good_key):
        # setup
        # disambiguate3
        this_key, expected_value = good_key

        # execute
        # assert isinstance(get_formal_name(this_key), str)#pass if it returns string. error will be key error
        # change structure of paramaterization list so that the value it returns is correct
        assert get_formal_name_v2(this_key) == expected_value


class TestUnhappyPath(object):

    @pytest.mark.parametrize('key_probs', [
        'bingus',
        'Apple',
        ' apple',
        'apple ',
        'appple',
        1,
        # [1, 2, 3, 'bingus'],
        True
    ])
    def test_key_error(self, key_probs):
        # assert not get_formal_name('bingus') #returns KeyError
        # assert not isinstance(get_formal_name("bingus"), str)
        with pytest.raises(KeyError):
            assert get_formal_name_v2(key_probs)

    @pytest.mark.parametrize('type_probs', [
        [1, 2, 3, 'bingus'],
    ])
    def test_type_error(self, type_probs):
        # assert not get_formal_name('bingus') #returns KeyError
        # assert not isinstance(get_formal_name("bingus"), str)
        with pytest.raises(TypeError):
            assert get_formal_name_v2(type_probs)

    def test_no_args(self):
        with pytest.raises(TypeError):
            get_formal_name_v2()

    def test_double_args(self):
        with pytest.raises(TypeError):
            get_formal_name_v2('apple', 'apple')
