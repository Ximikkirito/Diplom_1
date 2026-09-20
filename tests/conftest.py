import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


@pytest.fixture
def bun():
    return Bun("black bun", 100)


@pytest.fixture
def sauce():
    return Ingredient(
        INGREDIENT_TYPE_SAUCE,
        "hot sauce",
        100
    )


@pytest.fixture
def filling():
    return Ingredient(
        INGREDIENT_TYPE_FILLING,
        "cutlet",
        200
    )