#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
        
    def ObtenerCUIT(self):
        cuit=" "
        genero=input(print("Que genero sos"))
        if (genero == "m" or genero== "M"):
            cuit = "1-42477160"
        else:
            if (genero == "f" or genero =="F"):
               cuit = "2-42477160"
        return cuit

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()
    
    if id(s1) == id(s2):
        
        print(s1.ObtenerCUIT())
    else:
        print("Singleton failed, variables contain different instances.")