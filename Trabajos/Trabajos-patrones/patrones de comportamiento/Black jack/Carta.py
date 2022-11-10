from string import printable


class Carta:

    def __init__(self, valor, pinta) -> None:
        self._valor = valor
        self._pinta = pinta
    
    def getValor(self):
        return self._valor
    
    def getPinta(self):
        return self._pinta

    def __str__(self) -> str:
        return self._pinta