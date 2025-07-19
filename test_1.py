import pytest 

@pytest.mark.primarios
def test_par():
    assert 10 % 2 ==0
    

def test_impar():
    assert 10 % 3 ==1 