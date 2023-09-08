import pytest
from tarea_sumas import suma, sumar_lista

def test_suma():
    assert suma(1, 1) == 2
    assert suma(0, 0) == 0
    assert suma(-1, 1) == 0
    assert suma(-1, -1) == -2
    assert suma(5.5, 2.5) == 8.0

def test_sumar_lista():
    assert sumar_lista([1, 2, 3, 4, 5]) == 15
    assert sumar_lista([]) == 0
    assert sumar_lista([-1, 0, 1]) == 0
    assert sumar_lista([1.5, 2.5, 3.5]) == 7.5
    assert sumar_lista([10]) == 10
