import pytest
from src.ejercicio2_11 import repPalabra

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ("hola", "hola"),
      ("piedra", "piedra"),
      ("bolas", "bolas")
    ] 
)
def test_repPalabra_params(input_n1, expected):
    assert repPalabra(input_n1) == expected