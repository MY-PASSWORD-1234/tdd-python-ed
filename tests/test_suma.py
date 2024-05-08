# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import suma


class SumaTetsClass:

 
    def test_suma(self):
        assert suma(4,5) == 9
        assert suma(-1,-2) == -3
        assert suma(-7,5) == -2
        assert suma(-7,9) == 2
