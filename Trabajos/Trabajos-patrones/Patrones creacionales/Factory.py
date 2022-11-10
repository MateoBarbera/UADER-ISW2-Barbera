#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class FacturaA(Creator):


    def factory_method(self) -> Product:
        return FacturaA()

class FacturaB(Creator):
 

    def factory_method(self) -> Product:
        return FacturaB()

class FacturaC(Creator):


    def factory_method(self) -> Product:
        return FacturaC()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class FacturaA(Product):
    def operation(self) -> str:
        return "Factura A"


class FacturaB(Product):
    def operation(self) -> str:
        return "Factura B"


class FacturaC(Product):
    def operation(self) -> str:
        return "Factura C"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":

    print("\n\n")
    print("Tu Factura es")
    client_code(FacturaA())
    print("\n")

    print("Tu Factura es")
    client_code(FacturaB())

    
    print("Tu Factura es")
    client_code(FacturaC())