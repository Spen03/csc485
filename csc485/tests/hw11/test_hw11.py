import pytest
from csc485.projects.hw11.get_fruit_name import get_formal_name

"""
* Test that appended keys yield the correct response
** Strings that are in the dictionary of fruits
* Test that non-appended keys will yield a type or a key error 
** integers, mistakes in strings, bools, lists, and tuples
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
        # assert isinstance(get_formal_name(this_key), str)
        # #pass if it returns string. error will be key error
        # change structure of paramaterization-
        # -list so that the value it returns is correct
        assert get_formal_name(this_key) == expected_value


class TestUnhappyPath(object):

    @pytest.mark.parametrize('key_probs', [
        'bingus',
        'Apple',
        ' apple',
        'apple ',
        'appple',
        1,
        # [1, 2, 3, 'bingus'],
        True,
        ('apple', 2)
    ])
    def test_key_error(self, key_probs):
        # assert not get_formal_name('bingus') #returns KeyError
        # assert not isinstance(get_formal_name("bingus"), str)
        with pytest.raises(KeyError):
            assert get_formal_name(key_probs)

    @pytest.mark.parametrize('type_probs', [
        [1, 2, 3, 'bingus'],
    ])
    def test_type_error(self, type_probs):
        with pytest.raises(TypeError):
            assert get_formal_name(type_probs)

    def test_no_args(self):
        with pytest.raises(TypeError):
            get_formal_name()

    def test_double_args(self):
        with pytest.raises(TypeError):
            get_formal_name('apple', 'apple')
