from __future__ import annotations
from abc import ABC, abstractmethod


class Impresora:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def mandar_a_imprimir(self, imagen = "casa.jpg") -> str:
        print("Mandando a imprimir la imagen")
        return (f"{self.implementation.imprimir(imagen)}")



class Implementation(ABC):
    @abstractmethod
    def imprimir(self, imagen) -> str:
        pass

class ImpresoraBlancoNegro(Implementation):
    def imprimir(self, imagen) -> str:
        print("Transformando a blanco y negro...")
        print(self.transformar_blanco_negro(imagen))
        print("Imprimiendo...")
        return f"La imagen '{imagen}' fue impresa en blanco y negro."

    def transformar_blanco_negro(self, imagen):
        return f"La imagen '{imagen}' fue transformada a blanco y negro."


class ImpresoraColor(Implementation):
    def imprimir(self, imagen) -> str:
        print("Ajustando color...")
        print(self.ajustar_color(imagen))
        print("Imprimiendo...")
        return f"La imagen '{imagen}' se imprimio correctamente a color."

    def ajustar_color(self, imagen):
        return f"Los colores de la imagen '{imagen}' fueron ajustados."


def client_code(impresora: Impresora) -> None:
    print(impresora.mandar_a_imprimir(), end="")

if __name__ == "__main__":
    implementation = ImpresoraBlancoNegro()
    abstraction = Impresora(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ImpresoraColor()
    abstraction = Impresora(implementation)
    client_code(abstraction)

    print("\n")