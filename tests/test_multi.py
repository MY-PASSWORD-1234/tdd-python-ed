# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import multiplicacion


class TetsClass:

 
    def test_multi(self):
        assert multiplicacion(4,5) == 20
        assert multiplicacion(-1,-2) == 2
        assert multiplicacion(-7,5) == -35
        assert multiplicacion(-7,9) == -63