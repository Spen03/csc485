import pytest
from csc485.projects.hw12.compute_complexity import compute_complexity

"""
>test that the expected inputs return 100

>test that inputs not listed return 0

>test that combinations of good and bad return 100

>test other datatypes return type errors:
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
    {'~'},
    (1, '~')

])
def test_expected_char(character):
    # setup
    # disambiguate
    # execute
    assert compute_complexity(character) > 0


class TestMultipleArgs(object):

    def test_multiple_expected_char(self):
        assert compute_complexity('~@#')

    def test_good_and_bad(self):
        assert compute_complexity('~a')

    def test_bad_and_good(self):
        assert compute_complexity('a~')


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
def test_bad_input(excluded):
    # setup
    # disambiguate
    # execute
    assert compute_complexity(excluded) == 0


    #[1, 2, 3], #assertion
    #['~', '#'], #list with good characters #does not raise error, is it good?#its good
    #{'~'}, same with this
    #(1, '~') #this doesn't pass or raise type errors.
def test_bad_input_int():
    # [1, 2, 3], #assertion
    # ['~', '#'], #list with good characters #does not raise error, is it good?#its good
    # {'~'}, same with this
    # (1, '~') #this too.
    with pytest.raises(TypeError):
        assert compute_complexity(1)



def test_bad_input_list_of_int():

    with pytest.raises(AssertionError):
        assert compute_complexity([1, 2, 3])
