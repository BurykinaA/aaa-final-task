from typing import List, Dict, Union
from pizza import *


def full_menu_str() -> str:
    """Возвращает строку с полным меню."""
    menu = []
    for pizza in [Margherita, Pepperoni, Hawaiian]:  # Перебираем все доступные пиццы
        # Добавляем информацию о каждой пицце в меню
        menu.append(f"- {pizza.name()} {pizza.emoji} : {', '.join(pizza.ingredients)}")
    return "\n".join(menu)  # Возвращаем меню в виде строки


class Pizza:
    AVAILABLE_PIZZA_SIZES: List[str] = ["L", "XL"]  # Доступные размеры пиццы
    is_baked: bool  # Показывает, выпечена ли пицца
    is_delivered: bool  # Показывает, доставлена ли пицца
    is_pickup: bool  # Показывает, забрана ли пицца

    def __init__(self, size: str = "L") -> None:
        """Инициализирует пиццу с выбранным размером."""
        if size.upper() not in self.AVAILABLE_PIZZA_SIZES:
            string_error = "Извините, у нас нет такого размера"
            raise ValueError(string_error)
        self.size = size
        self.is_baked = False
        self.recipe = []

    def bake(self) -> None:
        """Выпекает пиццу."""
        self.is_baked = True

    def delivery(self) -> None:
        """Доставляет пиццу."""
        print("ddcf")
        self.is_delivered = True

    def pickup(self) -> None:
        """Забирает пиццу."""
        self.is_pickup = True

    @classmethod
    def name(cls) -> str:
        """Возвращает название пиццы."""
        pizza_name = cls.__name__
        return pizza_name

    def get_recipe(self) -> str:
        """Возвращает рецепт пиццы."""
        return ", ".join(self.recipe)

    def __str__(self) -> str:
        """Возвращает описание экземпляра пиццы."""
        return (
            f"{type(self).name()}, " f"Размер: {self.size}, Выпечена: {self.is_baked}"
        )

    def __repr__(self) -> str:
        """Возвращает представление пиццы с оригинальными параметрами. Она не будет выпечена."""
        return f"{type(self).__name__}(size={self.size!r})"

    def __eq__(self, other: object) -> bool:
        """Сравнивает пиццы по их характеристикам. Они будут равны только при одинаковом рецепте, размере и названии."""
        if not isinstance(other, Pizza):
            return NotImplemented
        return (
            (set(self.recipe) == set(other.recipe))
            & (self.name() == other.name())
            & (self.size == other.size)
        )

    def dict(self) -> Dict[str, Dict[str, str]]:
        """Возвращает словарь с ключом=название пиццы, значение=рецепт пиццы."""
        return {self.name(): self.get_recipe()}


class Margherita(Pizza):
    """Рецепт пиццы Маргарита."""

    emoji = "🧀"
    ingredients = ["tomato sauce", "mozzarella", "tomatoes"]

    def __init__(self, size: str = "L") -> None:
        """Инициализирует рецепт пиццы Маргарита с выбранным размером."""
        super().__init__(size)
        self.recipe = self.ingredients


class Pepperoni(Pizza):
    """Рецепт пиццы Пепперони."""

    emoji = "🍕"
    ingredients = ["tomato sauce", "mozzarella", "pepperoni"]

    def __init__(self, size: str = "L") -> None:
        """Инициализирует рецепт пиццы Пепперони с выбранным размером."""
        super().__init__(size)
        self.recipe = self.ingredients


class Hawaiian(Pizza):
    """Рецепт пиццы Гавайская."""

    emoji = "🍍"
    ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapples"]

    def __init__(self, size: str = "L") -> None:
        """Инициализирует рецепт пиццы Гавайская с выбранным размером."""
        super().__init__(size)
        self.recipe = self.ingredients
