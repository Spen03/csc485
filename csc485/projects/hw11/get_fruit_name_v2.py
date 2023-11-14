from csc485.projects.hw10.fruit_query_v2 import is_it_a_fruit

def get_formal_name_v2(fruit):
    """
    Get the scientific name for the supplied `fruit` common name.

    :param fruit: str, common name for a fruit
    :return formal_name: str, the formal name for the supplied fruit
    """
    fruit_dict = {
        'apple': 'Malus domestica',
        'banana': 'Musa acuminata',
        'orange': 'Citrus × sinensis',
        'strawberry': 'Fragaria × ananassa',
        'grape': 'Vitis vinifera',
        'pineapple': 'Ananas comosus',
        'mango': 'Mangifera indica',
        'blueberry': 'Vaccinium corymbosum',
        'peach': 'Prunus persica',
        'watermelon': 'Citrullus lanatus',
        'cherry': 'Prunus avium',
        'pear': 'Pyrus',
        'plum': 'Prunus domestica',
        'raspberry': 'Rubus idaeus',
        'kiwi': 'Actinidia deliciosa',
        'lemon': 'Citrus limon',
        'avocado': 'Persea americana',
        'pomegranate': 'Punica granatum',
        'cranberry': 'Vaccinium macrocarpon',
        'grapefruit': 'Citrus × paradisi'
    }

    if is_it_a_fruit(fruit):
        #make a new is it a fruit fucntion in here. dont import anything
        #make a method to normalize inputs, ie if you type capitals, still accept it
        return formal_name

    #print("Please enter a fruit in lowercase. Example: 'apple'")
    #return False
