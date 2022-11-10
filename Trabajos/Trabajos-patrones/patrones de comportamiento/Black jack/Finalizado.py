from Crupier import Crupier
from State import State
from Jugador import Jugador

class Finalizado(State):
    
    def iniciado(self, jugadores, crupier, mazo, puntajeMaximo)  -> None:
        print("El juego a finalizado...")

    def finalizado(self, jugadores, crupier, mazo, puntajeMaximo, blackjack):

        def getResultados(jugadoresR, crupierR, puntajeMaximoR):
            ganadores = []
            empates = []
            perdedores = []

            resultados = []

            for jugador in jugadoresR:
                
                if(jugador.getPuntaje() > puntajeMaximoR
                    or jugador.getPuntaje() < crupierR.getPuntaje()):
                    perdedores.append(jugador)
                elif jugador.getPuntaje() > crupierR.getPuntaje():
                    ganadores.append(jugador)
                elif jugador.getPuntaje() == crupierR.getPuntaje():
                    empates.append(jugador)
            
            resultados.append(ganadores)
            resultados.append(empates)
            resultados.append(perdedores)

            return resultados

        def mostrarResultados(resultados):
            
            print('Ganadores')
            if(len(resultados[0]) > 0):
                for jugador in resultados[0]:
                    print(jugador.showInfo(), "\n")
            else:
                print("No hay ganadores\n")
            print('\nEmpates')
            if(len(resultados[1]) > 0):
                for jugador in resultados[1]:
                    print(jugador.showInfo() + "\n")
            else:
                print("No hay empates con la banca\n")

            print('\nPerdedores')
            if(len(resultados[2]) > 0):
                for jugador in resultados[2]:
                    print(jugador.showInfo() + "\n")
            else:
                print("No hay empates con la banca\n")

        crupier.sumarPuntos()
        
        while(crupier.getPuntaje() < 16):
            crupier.templateAlgoritmo("1", crupier, mazo)
            crupier.sumarPuntos()

        if(crupier.getPuntaje() > puntajeMaximo):
            print("El crupier tiene ", crupier.getPuntaje(), 
                  " el cual es mayor al puntaje maximo ", puntajeMaximo,
                  "Por ende, todos los jugadores ganan")
        else:
            resultados = getResultados(jugadores, crupier, puntajeMaximo)
            mostrarResultados(resultados)

        op = input("\nPresione una tecla para continuar...")
        blackjack.menu()