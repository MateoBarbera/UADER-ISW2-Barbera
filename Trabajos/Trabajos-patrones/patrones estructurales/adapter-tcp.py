class Aplicacion:
    def request(self) -> str:
        return "La aplicacion tiene que recibir un mensaje desde el servidor."

#Adaptee
class Servidor:
    def specific_request(self) -> str:
        return "Mensaje encriptado: Mensaje desde el servidor"

#Adapter
class AdaptadorSerieTCP(Aplicacion, Servidor):
    def request(self) -> str:
        return f"Servidor: {self.specific_request()[20:]} "

if __name__ == "__main__":
    print("Llamando al servidor directamente: ")
    servidor = Servidor()
    print(servidor.specific_request())

    print()

    print("Llamado al servidor usando el adapter: ")
    servidor = AdaptadorSerieTCP()
    print(servidor.request())