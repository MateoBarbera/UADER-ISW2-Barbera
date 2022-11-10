from __future__ import annotations
from collections.abc import Iterable, Iterator
from random import shuffle
from Carta import Carta

class MazoIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: Mazo, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value
    
    def len(self):
        return (len(self._collection) - self._position)
    

class Mazo(Iterable):
    def __generarMazo__(self):

        valores = [{'carta' : '1', 'valor' : 1}, 
                    {'carta' : '2', 'valor' : 2},
                    {'carta' : '3', 'valor' : 3},
                    {'carta' : '4', 'valor' : 4},
                    {'carta' : '5', 'valor' : 5},
                    {'carta' : '6', 'valor' : 6},
                    {'carta' : '7', 'valor' : 7},
                    {'carta' : '8', 'valor' : 8},
                    {'carta' : '9', 'valor' : 9},
                    {'carta' : '10', 'valor' : 10},
                    {'carta' : 'J', 'valor' : 10},
                    {'carta' : 'Q', 'valor' : 10},
                    {'carta' : 'K', 'valor' : 10},
                    {'carta' : 'A', 'valor' : 11}
                    ]
        
        pintas = ['♠', '♥','♣', '♦️']

        mazo = []

        figura = ''

        for pinta in pintas:
            for valor in valores:
                figura = valor['carta'] + '' + pinta
                mazo.append(Carta(valor['valor'], figura))
        
        return mazo

    def __init__(self) -> None:
        self._mazo = self.__generarMazo__()
    
    def __iter__(self) -> MazoIterator:
        return MazoIterator(self._mazo)
    
    def getReverseIterator(self) -> MazoIterator:
        return MazoIterator(self._mazo, True)

    def mezclar(self):
        shuffle(self._mazo)

    def __str__(self) -> str:
        strMazo = ''
        for carta in self.getMazo():
            strMazo += carta.getPinta() + ' '
        
        return strMazo