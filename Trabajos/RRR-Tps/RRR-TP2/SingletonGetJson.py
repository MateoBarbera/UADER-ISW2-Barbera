from SingletonMeta import SingletonMeta

class SingletonGetJson(SingletonMeta):

    def getToken(tk, obj):
        clave = None
        if tk == 'token 1':
            clave = obj['token1']
        elif tk == 'token 2':
            clave = obj['token2']
        else:
            return 'el token ' + tk + ' no existe'

        return clave
            