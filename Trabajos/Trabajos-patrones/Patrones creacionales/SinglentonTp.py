from Singlenton import Singleton



s1 = Singleton()
s2 = Singleton()
    
if id(s1) == id(s2):
        
        print(s1.ObtenerCUIT())
else:   
        print("Singleton failed, variables contain different instances.")