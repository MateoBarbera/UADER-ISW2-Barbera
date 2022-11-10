import string

class VGA:
  
    def conexion(self)-> str:
       return  print ("conectado")
        
   

class HD :
    
    def serial_open(self) -> str:
        return "conectado atraves puerto VGA"
        
   


class AdapterVGA2HD(VGA, HD):

    def conexion(self) -> str:
        return f"Adapter:  {self.serial_open()}"
 
   

def sender(VGA: "VGA") :
    print(VGA.conexion())


def senderHD(HD: "HD") :
    print(HD.serial_open())






Vga = VGA()
sender(Vga)

hd = HD()
senderHD(hd)
adapter= AdapterVGA2HD()

sender( AdapterVGA2HD()
)