class SingletonMeta(type):
    """
    La clase Singleton puede ser implementada de diferentes formas en Python. Alguno
    de los metodos posibles incluyen: clase base, decorador, metaclase, etc. Nosotros
    usaremos las metaclases debido a que es la forma que mas se adecua para este 
    proposito.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Los cambios posibles para el valor del argumento '__init__' no afecta
        la instancia retornada.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Cualquier singleton debe definir alguna logica de negocio, la cual
        puede ser ejecutada en su instancia.
        """

        # ...
    
    def getid(self):
        return "MyUniqueID"

if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        print(s1.getid())
        
        print('Id 1: ', id(s1))
        print('Id 2: ', id(s2))
    else:
        print("Singleton failed, variables contain different instances.")