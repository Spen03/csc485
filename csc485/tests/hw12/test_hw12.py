import pytest
from csc485.projects.hw12.compute_complexity import compute_complexity

"""
>hw14 that the expected inputs return 100

>hw14 that inputs not listed return 0

>hw14 that combinations of good and bad return 100

>hw14 other datatypes return type errors:
>>integers, lists, tuples
>>>lists and tuples with good strings inside

"""


@pytest.mark.parametrize('character', [
    '~',
    '@',
    '#',
    '$',
    '%',
    '^',
    '&',
    '-',
    '_',
    '+',
    '=',
    ['~', '#'],
    {'~'}
    # (1, '~')

])
def test_expected_char_single(character):
    # setup
    # 100 is expected value for single characters
    # execute
    assert compute_complexity(character) == 100


class TestMultipleArgs(object):

    def test_multiple_special_char(self):
        assert compute_complexity('~@#') == 100

    def test_special_char_and_special_char(self):
        assert compute_complexity('~a') == 100

    def test_unspecial_char_and_special_char(self):
        assert compute_complexity('a~') == 100


@pytest.mark.parametrize('excluded', [
    'b',
    'i',
    'n',
    'g',
    'u',
    's',
    '1',
    '2',
    ' ',
    'A',
    ')'
])
def test_unspecial_char(excluded):
    # setup
    # 0 is expected because there isn't a special character
    # execute
    assert compute_complexity(excluded) == 0

    # [1, 2, 3], #assertion
    # ['~', '#'], #list with good characters #does not raise error, is it good?#its good
    # {'~'}, same with this
    # (1, '~') #this doesn't pass or raise type errors.


def test_incorrect_input_type_int():
    # [1, 2, 3], #assertion
    # ['~', '#'], #list with good characters #does not raise error, is it good?#its good
    # {'~'}, #same with this
    # (1, '~') #this too.
    with pytest.raises(TypeError):
        assert compute_complexity(1)


def test_incorrect_assertion_list_of_int():
    with pytest.raises(AssertionError):
        assert compute_complexity([1, 2, 3])


@pytest.mark.parametrize('passwords', [
    ('bingus~', 14.285714285714286),
    ('abc~@#', 50),
    'password123',
    'password@#$',
    'p@$$w0rD',
    '@lfr3dTh3Buttl3r',
    'gr1mace$h@k3',
    '~!@#$%^&*()',
    # make tuples of the password and their expected values
    # systematically include all of the complexifiers into your password
    # iterate through them
    # test even number and odd number passwords ie abc, abcd
    # equivalence class partitioning

])
def test_double_check_logic(passwords):
    """
    same code from compute complexity. This double-checks the logic,
    making sure the function gives us the values we expect
    """
    complexifiers = ['~', '@', '#', '$', '%', '^', '&', '-', '_', '+', '=']
    num_complexifiers = 0

    for char in passwords:
        if char in complexifiers:
            num_complexifiers = num_complexifiers + 1

    # compute the complexity
    length_of_data = len(passwords)
    complexity = (num_complexifiers * 100) / length_of_data

    assert compute_complexity(passwords) == complexity
