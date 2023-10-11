import pytest

from csc485.projects.hw12.compute_complexity import compute_complexity


@pytest.mark.parametrize('key', [
    '~', '@', '#', '$', '%', '^', '&', '-', '_', '+', '='
])
def test_good_key(key):
    # setup
    # disambiguate
    this_key = key

    # execute
    assert compute_complexity(this_key) == 100


@pytest.mark.parametrize('key', [
    'b', 'i', 'n', 'g', 'u', 's', '1', '2', ' ', 'A', ')'
])
def test_bad_key(key):
    # setup
    # disambiguate
    this_key = key

    # execute
    assert compute_complexity(this_key) == 0
