# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplicacion


class MultiTetsClass:

 
    def test_multi(self):
        assert multiplicacion(4,5) == 20
        assert multiplicacion(-1,3) == -3
        assert multiplicacion(-7,5) == -35
        assert multiplicacion(-7,2) == -14