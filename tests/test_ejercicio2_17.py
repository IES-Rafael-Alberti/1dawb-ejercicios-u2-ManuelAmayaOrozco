import pytest
from src.ejercicio2_17 import tablasMultiplicar

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (1, "1 x 10 = 10"),
      (8, "8 x 10 = 80"),
      (10, "10 x 10 = 100")
    ] 
)
def test_tablasMultiplicar_params(input_n1, expected):
    assert tablasMultiplicar(input_n1) == expected