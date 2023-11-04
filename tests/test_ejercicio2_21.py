import pytest
from src.ejercicio2_21 import letraPalab

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ("hola", ""),
      ("melocotón", ""),
      ("aguacate", "")
    ] 
)
def test_letraPalab_params(input_n1, expected):
    assert letraPalab(input_n1) == expected