import pytest 
from abreviatura import abreviatura

@pytest.mark.parametrize("nome,abrev",[("Fernado Santos","FS"),
                                ("Renata Franco","RF"),("Renato Gonçalves","RG")])

def test_abreviatura(nome,abrev):
    assert abreviatura(nome) == abrev
