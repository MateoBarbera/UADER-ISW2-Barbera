class Impresora:
    def imprimir(self, imagen='casa.jpg') -> str:
        print('Imprimiendo en impresora a color...')
        return f"La imagen '{imagen}' se imprimio correctamente a color."

class ImpresoraBlancoNegro:
    def imprimir_blanco_negro(self, imagen = 'casa.jpg', blanco_negro = False) -> str:
        if blanco_negro:
            return f"La imagen '{imagen}' se imprimio correctamente en blanco y negro."
        else:
            return("No se pudo imprimir la imagen, no se puede imprimir a color en esta impresora.")

class AdaptadorBlancoNegro(Impresora, ImpresoraBlancoNegro):
    def imprimir(self, imagen = 'casa.jpg') -> str:
        print(f"Convirtiendo '{imagen}' a blanco y negro...")
        print('Imprimiendo en impresora en blanco y negro...')
        return(self.imprimir_blanco_negro(imagen, True))

def mandar_a_imprimir( impresora : 'Impresora', imagen = 'casa.jpg' ):
    print(impresora.imprimir(imagen))

#### MAIN ####
if __name__ == "__main__":
    print("Mandar a imprimir una foto de una casa a color a la impresora a color...")
    impresora = Impresora()
    mandar_a_imprimir(impresora, 'casa.jpg')
    print("\n")

    print("Mandar a imprimir una foto de una casa a color a la impresora en blanco y negro...")
    impresora = ImpresoraBlancoNegro()
    print(impresora.imprimir_blanco_negro('casa.jpg'))
    print("\n")

    print("Mandar a imprimir una foto de una casa a color a la impresora en blanco y negro mediante el adaptador...")
    impresora = AdaptadorBlancoNegro()
    mandar_a_imprimir(impresora, 'casa.jpg')
    print("\n")