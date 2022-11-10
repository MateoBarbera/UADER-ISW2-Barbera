#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def factura(self) -> None:
        pass

    @abstractmethod
    def producto_a(self) -> None:
        pass

    @abstractmethod
    def producto_b(self) -> None:
        pass

    @abstractmethod
    def producto_c(self) -> None:
        pass


class FacturaVentaBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._factura = Factura()

    @property
    def factura(self) -> Factura:
        factura = self._factura
        self.reset()
        return factura

    def producto_a(self) -> None:
        self._factura.add("ProductoA1")

    def producto_b(self) -> None:
        self._factura.add("ProductoB1")

    def producto_c(self) -> None:
        self._factura.add("ProductoC1")


class Factura():
    def __init__(self) -> None:
        self.productos = []

    def add(self, producto: Any) -> None:
        self.productos.append(producto)

    def lista_productos(self) -> None:
        print(f"Lista de productos: {', '.join(self.productos)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def factura_venta_todos(self) -> None:
        self.builder.producto_a()
        self.builder.producto_b()
        self.builder.producto_c()