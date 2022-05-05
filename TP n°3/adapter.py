#*--------------------------------------------------
#* adapter.py
#* excerpt from https://refactoring.guru/design-patterns/adapter/python/example
#*--------------------------------------------------

class Target:
    """
    El destino define la interfaz específica del dominio utilizada por el código del cliente.

    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    El Adaptee contiene algunos comportamientos útiles, pero su interfaz es incompatible
    con el código de cliente existente. El Adaptado necesita alguna adaptación antes de que el
    el código del cliente puede usarlo.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    El Adaptador hace que la interfaz del Adaptado sea compatible con la interfaz del Destino a través de la herencia múltiple.

    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    El código del cliente admite todas las clases que siguen la interfaz de Target.

    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
