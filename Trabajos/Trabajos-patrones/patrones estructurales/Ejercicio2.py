import string

class Http:
  
    def open(self)-> str:
       return  print ("abierto el puerto 443")
        
    def put(self)-> str:
        return print("enviando por post")
       
    def close(self)->str:
       return print("cerrando puerto 443")


class Serial :
    
    def serial_open(self) -> str:
        return "abierto puerto serie 387"
        
    def serial_put(self) -> str:
        return "enviando puerto serie 387"
        
    def serial_close(self) -> str:
        return "cerrando puerto serie 387"
    


class AdapterHttp2Serial(Http, Serial):

    def open(self) -> str:
        return f"Adapter:  {self.serial_open()}"
 
    def put(self) -> str:
        return f"Adapter:  {self.serial_put()}"
        
    def close(self) -> str:
        return f"Adapter:  {self.serial_close()}"
        

def sender(http: "Http") :
    print(http.open())
    print(http.put())
    print(http.close())



http = Http()
sender(http)

adapter= AdapterHttp2Serial()

sender(adapter)