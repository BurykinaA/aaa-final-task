import pytest
from pizza import *


def test_pizza_init():
    """Тестирование инициализации пиццы."""
    pizza = Pizza("L")
    assert pizza.size == "L"
    assert pizza.is_baked == False


def test_pizza_bake():
    """Тестирование выпечки пиццы."""
    pizza = Pizza("L")
    pizza.bake()
    assert pizza.is_baked == True


def test_pizza_delivery():
    """Тестирование доставки пиццы."""
    pizza = Pizza("L")
    pizza.delivery()
    assert pizza.is_delivered == True


def test_pizza_pickup():
    """Тестирование забора пиццы."""
    pizza = Pizza("L")
    pizza.pickup()
    assert pizza.is_pickup == True


def test_pizza_name():
    """Тестирование имени пиццы."""
    pizza = Pizza("L")
    assert pizza.name() == "Pizza"


def test_pizza_get_recipe():
    """Тестирование получения рецепта пиццы."""
    pizza = Pizza("L")
    assert pizza.get_recipe() == ""


def test_pizza_str():
    """Тестирование строкового представления пиццы."""
    pizza = Pizza("L")
    assert str(pizza) == "Pizza, Размер: L, Выпечена: False"


def test_pizza_repr():
    """Тестирование представления пиццы."""
    pizza = Pizza("L")
    assert repr(pizza) == "Pizza(size='L')"


def test_pizza_eq():
    """Тестирование равенства пицц."""
    pizza1 = Margherita("L")
    pizza2 = Margherita("L")
    assert (pizza1 == pizza2) == True


def test_pizza_dict():
    """Тестирование словарного представления пиццы."""
    pizza = Pizza("L")
    assert pizza.dict() == {"Pizza": ""}


def test_full_menu_str():
    """Тестирование полного меню."""
    menu = full_menu_str()
    assert "Margherita" in menu
    assert "Pepperoni" in menu
    assert "Hawaiian" in menu
