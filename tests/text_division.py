# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import division


class DivisionTetsClass:

 
    def test_division(self):
        assert division(10,5) == 2.0
        assert division(100,10) == 10.0
        assert division(5,1) == 5.0
        assert division(7,2) == 3.5
        #