from pickletools import OpcodeInfo
from turtle import delay
from Crupier import Crupier
from Iniciado import Iniciado
from Jugador import Jugador
from State import Context


from Mazo import Mazo

class BlackJack:
    
    def __init__(self) -> None:
        self._nombreJugadores = []
        self._recienInicio = True
    
    def menu(self):
        opcion = "0"
        jugadores = []
        
        while(opcion not in ["1", "2"]):
            opcion = input("1-Iniciar Juego\n2-Salir\n\nElegir: ")
            
            if(opcion == "1"):
                if self._recienInicio:
                    self._nombreJugadores = self.intro()
                    self._recienInicio = False
                
                for nombre in self._nombreJugadores:
                    jugadores.append(Jugador(nombre))

                self.blackJackGame(jugadores)
            if(opcion == "2"):
                print("Nos vemos!!!")
                delay(1000)

    def blackJackGame(self, jugadores):
        puntajeMaximo = 21
        mazo = Mazo()
        mazo.mezclar()
        cMazo = mazo.__iter__()
        crupier = Crupier('Emiliano')

        contexto = Context(Iniciado())
        contexto.request1(jugadores, crupier, cMazo, puntajeMaximo)
        contexto.request2(jugadores, crupier, cMazo, puntajeMaximo, self)

    def intro(self):
        cantJugadores = 3
        nombreJugadores = []

        for i in range(0, cantJugadores):
            nombre = input("Ingrese el nombre del jugador N°" + str(i) + ": ")
            nombreJugadores.append(nombre)
        
        return nombreJugadores