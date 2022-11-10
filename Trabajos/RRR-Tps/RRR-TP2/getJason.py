# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Warning: this version of Python has problems handling the Python 3 byte type in constants properly.

# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55




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
        

class SingletonParaObtenerJson():
    __metaclass__ = SingletonMeta;

    def __init__(self):
        with open(jsonfile, 'r') as (myfile):
            data = myfile.read()
            self.token =json.loads(data)
        

    def getData(self):
        return self.token

        
        

import json, sys


version='1.0'
print('la cantidad de argumentos es: '+ str(len(sys.argv)))
print('los argumentos son: '+str(sys.argv))



if len(sys.argv)==1:
    print('no se puede ejecutar')
    print("Ruta",sys.argv)
    sys.exit()

if len(sys.argv)==2:
    
    data = sys.argv;
    a = SingletonParaObtenerJson(data)
    jsonfile = sys.argv[1]
    print("Token",a.getData(jsonfile));

else:
    jsonkey = sys.argv[2]

  
jsonfile = sys.argv[1]

print("Token",a.getData(jsonfile));