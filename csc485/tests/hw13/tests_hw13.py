from csc485.projects.hw13.homework13 import evaluate_strength
import pytest

"""
copy the tests from hw12 over to cover compute_complexity

test if evaluate strength returns an expected value, true or false
>parameterize a dictionary with passwords and expected values.
>I decided that I would not exhaustively test the happy path

test if incorrect input types return a type error
>Strangely, lists would give me an unexpected TypeError
-that would crash instead of
-passing, which was what I was looking for. Very strange.
"""


@pytest.mark.parametrize('passwords', {
    ('#', True),
    ('@bc#$%', True)
})
def test_password_value(passwords):
    this_password, expected_strength = passwords
    actual_strength = evaluate_strength(this_password)
    assert actual_strength == expected_strength


def test_unhappy_password():
    assert evaluate_strength('bingus') is False


@pytest.mark.parametrize('bad_type', {
    # ['#'],
    # {'abc'}
    1,
    ('a', 'b')
})
def test_bad_type(bad_type):
    with pytest.raises(TypeError):
        assert evaluate_strength(bad_type)
