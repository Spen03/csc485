from csc485.projects.hw11.getFruitName import get_formal_name


"""
test that when the function recieves a key it knows,
it will return the formal name

test that if it isn't a string,
return that the function accepts fruits
"""


class TestHappyPath(object):
    def test_apple(self):
        assert get_formal_name('apple') == 'Malus domestica'


class TestUnhappyPath(object):
    def test_not_fruit(self):
        assert not get_formal_name('bingus') #returns KeyError