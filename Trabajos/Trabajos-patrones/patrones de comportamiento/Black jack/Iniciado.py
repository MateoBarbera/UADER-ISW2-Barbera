from Finalizado import Finalizado
from Mazo import Mazo
from State import State
import os

class Iniciado(State):
    
    def iniciado(self, jugadores, crupier, mazo, puntajeMaximo)  -> None:
        def repatirCartas(jugadoresR, crupierR, mazoR):

            for i in range(0, 2):
                for jugador in jugadoresR:
                    jugador.addCarta(jugador.sacarCarta(mazoR, crupierR))
                crupierR.addCarta(crupier.sacarCarta(mazoR, crupierR))
        
        finGame = False
        opcion = "0"

        repatirCartas(jugadores, crupier, mazo)

        while(not finGame):
            for jugador in jugadores:
                if ((jugador.getPuntaje() <= puntajeMaximo)
                    and (not jugador.getPlantado())):

                    print(crupier.getNombre(), " ", crupier.getCartas()[0].getPinta() + "\n")
                    print(jugador.getNombre(), " ", jugador.getSCartas() + "\n")

                    opcion = input("1-Pedir carta\n2-plantarse\n\nElegir: ")
                    jugador.templateAlgoritmo(opcion, crupier, mazo)
                    jugador.sumarPuntos()
                    opcion = "0"

            
            for jugador in jugadores:

                if (jugador.getPlantado()
                    or (jugador.getPuntaje() > puntajeMaximo)):

                    finGame = True
                else:
                    finGame = False
                    break
        
        self.context.transition_to(Finalizado())
        
    def finalizado(self, jugadores, crupier, mazo, puntajeMaximo, blackjack):
        input("El juego esta en curso")