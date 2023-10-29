import pytest
from src.ejercicio2_3 import division

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (4, 2, 2.0),
      (4, 0, "Error, no se puede dividir por 0."),
      (6, 3, 2.0)
    ] 
)
def test_division_params(input_n1, input_n2, expected):
    assert division(input_n1, input_n2) == expected