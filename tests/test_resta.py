# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import resta


class RestaTetsClass:

 
    def test_resta(self):
        assert resta(4,5) == -1
        assert resta(-1,3) == 2
        assert resta(-7,5) == -2
        assert resta(-7,2) == -5