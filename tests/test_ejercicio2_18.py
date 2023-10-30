import pytest
from src.ejercicio2_18 import piramNum

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (3, ""),
      (5, ""),
      (8, "")
    ] 
)
def test_piramNum_params(input_n1, expected):
    assert piramNum(input_n1) == expected