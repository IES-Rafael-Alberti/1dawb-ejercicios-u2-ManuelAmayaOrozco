import pytest
from src.ejercicio2_16 import asterTriangulo

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (3, "***"),
      (8, "********"),
      (10, "**********")
    ] 
)
def test_asterTriangulo_params(input_n1, expected):
    assert asterTriangulo(input_n1) == expected