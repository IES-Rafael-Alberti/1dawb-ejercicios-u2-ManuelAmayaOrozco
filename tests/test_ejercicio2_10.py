import pytest
from src.ejercicio2_10 import pizzatime

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ("V", "V"),
      ("N", "N"),
      ("N", "N")
    ] 
)
def test_pizzatime_params(input_n1, expected):
    assert pizzatime(input_n1) == expected