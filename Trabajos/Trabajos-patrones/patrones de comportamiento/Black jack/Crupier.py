from Integrante import Integrante


class Crupier(Integrante):
    def __init__(self, nombre) -> None:
        super().__init__(nombre, 'crupier')

    def sacarCarta(self, mazo, crupier = None):
        carta = None
        cMazo = mazo.__iter__()
        if(cMazo.len() > 0):
            carta = cMazo.__next__()

        
        return carta
