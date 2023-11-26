import click
from pizza import *
from decorator import log

# Доступные пиццы
AVAILABLE_PIZZA = {
    "margherita": Margherita(),
    "pepperoni": Pepperoni(),
    "hawaiian": Hawaiian(),
}


@click.group()
def cli() -> None:
    """Добро пожаловать в пиццерию!"""


@log("🛵 Доставлено за {} сек!")
def deliver(pizza: Pizza) -> None:
    """Доставляет пиццу"""
    pizza.delivery()


@log("🏠 Забрали за {} сек!")
def pickup(pizza: Pizza) -> None:
    """Самовывоз пиццы"""
    pizza.pickup()


@log("🍕 Выпечено за {} сек!")
def bake(pizza: Pizza) -> None:
    """Выпекает пиццу"""
    pizza.bake()


@cli.command()
def menu() -> None:
    """Выводит доступную еду."""
    print(full_menu_str())


@click.command()
@click.option("--delivery", is_flag=True, help="Опция доставки.")
@click.option("--size", default="L")
@click.argument("pizza")
def order(pizza: str, delivery: bool, size: str) -> None:
    """Заказывает пиццу"""
    if pizza.lower() not in AVAILABLE_PIZZA.keys():
        print("Такой пиццы нет")
    pizza = AVAILABLE_PIZZA[pizza.lower()]
    print(*pizza.dict())
    bake(pizza)
    deliver(pizza) if delivery else pickup(pizza)


cli.add_command(order)

if __name__ == "__main__":
    cli()
