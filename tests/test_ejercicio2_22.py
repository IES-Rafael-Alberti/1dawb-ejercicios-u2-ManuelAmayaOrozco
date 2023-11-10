import pytest
from src.ejercicio2_22 import cuentaLetra

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      ("hooola", "o", "La letra se repite 3 veces."),
      ("Contar es muy facil", "a", "La letra se repite 2 veces."),
      ("xdxdxdxdxd", "x", "La letra se repite 5 veces.")
    ] 
)
def test_cuentaLetra_params(input_n1, input_n2, expected):
    assert cuentaLetra(input_n1, input_n2) == expected