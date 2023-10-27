import pytest
from src.ejercicio2_2 import tPassword

@pytest.mark.parametrize(
  "input_n1, expected",
    [
      ("holakase", False),
      ("contraseña", True),
      ("waswas", False)
    ] 
)
def test_tPassword_params(input_n1, expected):
    assert tPassword(input_n1) == expected