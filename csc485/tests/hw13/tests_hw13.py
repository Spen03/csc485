from csc485.projects.hw13.homework13 import evaluate_strength
import pytest

"""
* didn't extensively test happy path

* dict(password : value)
50, 49, 48...0 False
51, 52, 53...100 True

* incorrect input type = type error

* lists = TypeError (not passed by pytest)
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


@pytest.mark.parametrize('complexity_password', {
    (('x' * 100 + '@' * 0), False),
    (('x' * 99 + '@' * 1), False),
    (('x' * 51 + '@' * 49), False),
    (('x' * 50 + '@' * 50), False),
    (('x' * 49 + '@' * 51), True),
    (('x' * 1 + '@' * 99), True),
    (('x' * 0 + '@' * 100), True)
})
def test_response_range(complexity_password):
    feed_string, score = complexity_password
    assert evaluate_strength(feed_string) == score
