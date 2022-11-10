from random import shuffle
from Carta import Carta
from Crupier import Crupier
from Iniciado import Iniciado
from Mazo import Mazo
from Integrante import Integrante
from Jugador import Jugador
from State import Context

def testJugador():
    c1 = Carta(11, 'A')
    c2 = Carta(10, 'J')
    c3 = Carta(2, '2')

    jugador = Integrante('Blanchet', 'Bua')
    jugador.addCarta(c1)
    jugador.addCarta(c2)
    jugador.addCarta(c3)
    jugador.addCarta(c1)
    jugador.addCarta(c3)
    jugador.sumarPuntos()

    print(jugador.showInfo())

def testJugador2():
    mazo = Mazo()
    crupier = Crupier('Thomas')
    j1 = Jugador('Blanchet')

    j1.templateAlgoritmo("1", crupier, mazo)
    j1.sumarPuntos()
    print(j1.showInfo())

def testIterator():
    mazo =  Mazo()
    cMazo = mazo.__iter__()
    
    print("len mazo: ", cMazo.len(), "\n")

    while(cMazo.len() > 0):
        print(cMazo.__next__())

    print("len mazo: ", cMazo.len(), "\n")

def testState():
    puntajeMaximo = 21
    jugadores = [Jugador('Blanchet'), Jugador('Bua'), Jugador('Fernando')]
    mazo = Mazo()
    mazo.mezclar()
    cMazo = mazo.__iter__()

    crupier = Crupier('Marcos')

    contexto = Context(Iniciado())
    contexto.request1(jugadores, crupier, cMazo, puntajeMaximo)
    contexto.request2(jugadores, crupier, cMazo, puntajeMaximo)


# print("test 1")
# testJugador()

# print("\ntest 2")
# testJugador2()

# print("\ntest 3")
# testIterator()

testState()