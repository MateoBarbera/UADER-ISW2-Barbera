from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        # print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self, jugadores, crupier, mazo, puntajeMaximo):
        self._state.iniciado(jugadores, crupier, mazo, puntajeMaximo)

    def request2(self, jugadores, crupier, mazo, puntajeMaximo, blackjack):
        self._state.finalizado(jugadores, crupier, mazo, puntajeMaximo, blackjack)

class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def iniciado(self, jugadores, crupier, mazo):
        pass
    
    @abstractmethod
    def finalizado(self, jugadores, crupier, mazo, puntajeMaximo, blackjack):
        pass