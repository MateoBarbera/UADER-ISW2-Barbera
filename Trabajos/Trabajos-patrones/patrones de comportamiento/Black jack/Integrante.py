from abc import ABC
from Carta import Carta

#template
class Integrante(ABC):
    
    def __init__(self, nombre, rol) -> None:
        self._nombre = nombre
        self._rol = rol
        self._puntaje = 0
        self.cartas = []
        self._plantado = False
    
    def templateAlgoritmo(self, opcion, crupier, mazo):
        if opcion == "1":
            carta = self.sacarCarta(mazo, crupier)
            self.addCarta(carta)
        elif opcion == "2":
            self.sumarPuntos()
            self._plantado = True

    def showInfo(self):
        info = ("nombre: " + self._nombre 
                + "\npuntos: " + str(self._puntaje)
                + "\n" + self.getSCartas())

        return info

    def getNombre(self):
        return self._nombre
    
    def getRol(self):
        return self._rol
    
    def getPuntaje(self):
        return self._puntaje
    
    def getCartas(self):
        return self.cartas
    
    def getSCartas(self):
        misCartas = ""
        for carta in self.cartas:
            misCartas += carta.getPinta() + " "
        return misCartas

    def getPlantado(self):
        return self._plantado
    
    def addCarta(self, carta):
        if carta is not None:
            self.cartas.append(carta)

    def setPuntaje(self, puntaje):
        self._puntaje = puntaje

    def sumarPuntos(self):
        contPuntos = 0
        cantCartasAs = 0

        for carta in self.cartas:
            if (carta.getPinta()[0] != 'A'):
                contPuntos += carta.getValor()
            else:
                cantCartasAs += 1
        
        if cantCartasAs > 0:
            for i in range(0, cantCartasAs):
                if(contPuntos > 10):
                    contPuntos += 1
                else:
                    contPuntos += 11

        self.setPuntaje(contPuntos)
    
    def sacarCarta(self, mazo, crupier = None):
        pass