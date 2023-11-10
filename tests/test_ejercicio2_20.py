import pytest
from src.ejercicio2_20 import numPrimo

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (3, True),
      (5, True),
      (8, False)
    ] 
)
def test_numPrimo_params(input_n1, expected):
    assert numPrimo(input_n1) == expected