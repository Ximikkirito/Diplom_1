from unittest.mock import MagicMock

from praktikum.burger import Burger


def test_set_buns():
    burger = Burger()

    bun = MagicMock()

    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient():
    burger = Burger()

    ingredient = MagicMock()

    burger.add_ingredient(ingredient)

    assert ingredient in burger.ingredients


def test_remove_ingredient():
    burger = Burger()

    ingredient = MagicMock()

    burger.add_ingredient(ingredient)

    burger.remove_ingredient(0)

    assert burger.ingredients == []


def test_move_ingredient():
    burger = Burger()

    ingredient1 = MagicMock()
    ingredient2 = MagicMock()
    ingredient3 = MagicMock()

    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)

    burger.move_ingredient(2, 0)

    assert burger.ingredients == [
        ingredient3,
        ingredient1,
        ingredient2
    ]


def test_get_price():
    burger = Burger()

    bun = MagicMock()
    bun.get_price.return_value = 100

    ingredient1 = MagicMock()
    ingredient1.get_price.return_value = 50

    ingredient2 = MagicMock()
    ingredient2.get_price.return_value = 70

    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)

    assert burger.get_price() == 320


def test_get_receipt():
    burger = Burger()

    bun = MagicMock()

    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    ingredient = MagicMock()

    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    expected = (
        "(==== black bun ====)\n"
        "= sauce hot sauce =\n"
        "(==== black bun ====)\n\n"
        "Price: 250"
    )

    assert burger.get_receipt() == expected