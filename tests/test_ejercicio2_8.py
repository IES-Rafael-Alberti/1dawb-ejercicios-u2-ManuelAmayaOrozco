import pytest
from src.ejercicio2_8 import rendimiento

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (0.0, 0.0),
      (0.5, 1200.0),
      (0.8, 1920.0)
    ] 
)
def test_rendimiento_params(input_n1, expected):
    assert rendimiento(input_n1) == expected