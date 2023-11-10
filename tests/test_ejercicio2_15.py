import pytest
from src.ejercicio2_15 import capital

@pytest.mark.parametrize(
    "input_n1, input_n2, input_n3, expected",
    [
      (12, 2, 3, 12.734496),
      (14, 4, 2, 15.1424),
      (30, 4, 2, 32.44800000000001)
    ] 
)
def test_capital_params(input_n1, input_n2, input_n3, expected):
    assert capital(input_n1, input_n2, input_n3) == expected