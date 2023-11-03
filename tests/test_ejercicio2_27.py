import pytest
from src.ejercicio2_27 import sumDigs

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (10, "La suma de los dígitos es 1"),
      (123, "La suma de los dígitos es 6"),
      (456, "La suma de los dígitos es 15")
    ] 
)
def test_tablasMultiplicar_params(input_n1, expected):
    assert sumDigs(input_n1) == expected