import pytest
from src.ejercicio2_30 import searchPhrase

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      ("hola muy buenas", "u", "Se encontró coincidencia en la posición 6."),
      ("hola muy buenas", "x", "No se encontraron coincidencias en la frase."),
      ("hola muy buenas", "y", "Se encontró coincidencia en la posición 7.")
    ] 
)
def test_searchPhrase_params(input_n1, input_n2, expected):
    assert searchPhrase(input_n1, input_n2) == expected