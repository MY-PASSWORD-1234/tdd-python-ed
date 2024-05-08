# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta


class RestaTetsClass:

 
    def test_resta(self):
        assert resta(4,5) == -1
        assert resta(-1,-2) == 1
        assert resta(-7,5) == -12
        assert resta(-7,9) == -16