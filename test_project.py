import os
import pytest
from unittest.mock import patch
from menu_creator import create_menu, select_greeting_language, select_currency

def test_create_menu():

    menu_items = {
        'Dish1': ('Starters', '10'),
        'Dish2': ('Drinks', '5'),
        'Dish3': ('Dessert', '8')
    }
    restaurant_name = 'Test Restaurant'
    greeting = 'english'
    currency = 'dollar'
    file_name = f"{restaurant_name.lower().replace(' ', '_')}_menu.txt"


    create_menu(menu_items, restaurant_name, greeting, currency, file_name)



    assert os.path.exists(file_name)



def test_select_greeting_language():



    with patch('builtins.input', return_value='english'):
        result = select_greeting_language()
        assert result == 'english'


    with patch('builtins.input', return_value='turkish'):
        result = select_greeting_language()
        assert result == 'turkish'


    with patch('builtins.input', side_effect=['invalid_language', 'stop']):
        result = select_greeting_language()
        assert result is None



def test_select_currency():



    with patch('builtins.input', return_value='dollar'):
        result = select_currency()
        assert result == 'dollar'


    with patch('builtins.input', return_value='euro'):
        result = select_currency()
        assert result == 'euro'

    
    with patch('builtins.input', side_effect=['invalid_currency', 'stop']):
        result = select_currency()
        assert result is None


