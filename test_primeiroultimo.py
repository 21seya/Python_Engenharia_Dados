import pytest 
from Primeiroultimo import primeiroultimo 

@pytest.mark.parametrize("nomecompleto,resultado",[("Sophia Lima","Sophia Lima"),
                                ("Maria Duarte Santos","Maria Santos"),
                                ("Carla Peixoto Santos","Carla Santos")])

def test_primeiroultimo(nomecompleto,resultado):
    assert primeiroultimo(nomecompleto) == resultado
    