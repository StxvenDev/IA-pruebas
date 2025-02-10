import pytest
from division import dividir

# @pytest.fixture
# def 

def test_dividir_exception():
  with pytest.raises(ValueError) as excinfo:
    dividir(10,0)
  assert str(excinfo.value) == "No se puede dividir entre 0"

@pytest.mark.parametrize("a, b, result",[
  (10, 2, 5),
  (9, 3, 3),
  (20, 4, 5)
])
def test_divir(a,b,result):
  assert dividir(a,b) == result


