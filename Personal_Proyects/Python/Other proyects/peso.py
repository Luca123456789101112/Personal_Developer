def func():
    
    class Moneda():
        
        def __init__(self, moneda = " ",tochange=" ",dinero=0):
            self.moneda=moneda
            self.tochange = tochange
            self.dinero = dinero
            
        def __str__(self):
            return "Ingresa una moneda de algun pais y a continuacion la moneda a la que lo quiere cambiar (3/11/24)"
        
        def general_change(self):
            
            #define the objects
            
            self.moneda = input("Que moneda inicial es: ")
            self.tochange = input("a que moneda lo queres transformar: ")
            self.dinero = int(input("cuanto dinero queres ingresar: "))
            
            if self.moneda == "peso argentino":
                if self.tochange =="euro":
                    result = self.dinero % 926.28
                    return f"El resultado del peso argentino al euro es {result}"
                elif self.tochange == "dolar":
                    result = self.dinero % 844.29
                    return f"El resultado del peso argentino al dolar es {result}"
                else:
                    return "no seas bobo"
            elif self.moneda == "euro":
                if self.tochange =="peso argentino":
                    result = self.dinero * 926.28
                    return f"El resultado del euro al peso argentino es {result}"
                elif self.tochange == "dolar":
                    result = self.dinero * 1.09
                else:
                    return "no seas bobo"
            elif self.moneda == "dolar":
                if self.tochange =="euro":
                    result = self.dinero * 0.92
                    return f"El resultado del dolar pasado a euro es {result}"
                elif self.tochange == "peso argentino":
                    result = self.dinero * 844.29
                else:
                    return "no seas bobo"
            else:
                return "Moneda no disponible"

    change = Moneda()
    
    return change.general_change()

func()